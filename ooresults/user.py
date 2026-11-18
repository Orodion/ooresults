# Copyright (C) 2022 Rainer Garus
#
# This file is part of the ooresults Python package, a software to
# compute results of orienteering events.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import base64
import hashlib
import hmac
import json
import logging
import os
import pathlib
import secrets
import threading
import time
from typing import Optional

import jsonschema


SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "username": {"type": "string"},
            "password": {"type": "string"},
        },
        "required": ["username", "password"],
        "additionalProperties": False,
    },
}

# parameters of the scrypt password hash
SCRYPT_N = 2**14
SCRYPT_R = 8
SCRYPT_P = 1
SCRYPT_DKLEN = 32
HASH_PREFIX = "scrypt$"


def _b64encode(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def hash_password(password: str) -> str:
    """Return the scrypt hash of the password as stored in users.json.

    Format: scrypt$<n>$<r>$<p>$<salt (base64)>$<hash (base64)>
    """
    salt = secrets.token_bytes(16)
    dk = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P,
        dklen=SCRYPT_DKLEN,
    )
    return f"{HASH_PREFIX}{SCRYPT_N}${SCRYPT_R}${SCRYPT_P}${_b64encode(salt)}${_b64encode(dk)}"


def is_hashed(stored: str) -> bool:
    return stored.startswith(HASH_PREFIX) and len(stored.split("$")) == 6


def verify_password(password: str, stored: str) -> bool:
    """Check a password against a stored scrypt hash or plain text password."""
    if not is_hashed(stored):
        return hmac.compare_digest(password.encode("utf-8"), stored.encode("utf-8"))
    try:
        _, n, r, p, salt, dk = stored.split("$")
        expected = base64.b64decode(dk, validate=True)
        computed = hashlib.scrypt(
            password.encode("utf-8"),
            salt=base64.b64decode(salt, validate=True),
            n=int(n),
            r=int(r),
            p=int(p),
            dklen=len(expected),
        )
    except ValueError:
        logging.error("Invalid password hash in users.json")
        return False
    return hmac.compare_digest(computed, expected)


def _write_users(path: pathlib.Path, users: list[dict[str, str]]) -> None:
    """Write users.json readable only by the owner (on Linux and macOS)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(path.name + ".tmp")
    fd = os.open(tmp_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(users, f, indent=4)
    os.replace(tmp_path, path)


class Users:
    sema = threading.Semaphore()
    path: Optional[pathlib.Path] = None
    # username -> password hash (or plain text password if not yet hashed)
    users: dict[str, str] = {}
    # successfully checked credentials, to avoid computing the expensive
    # password hash for each request; the keys are HMACs with a random key
    _cache_key = secrets.token_bytes(32)
    _verified: set[bytes] = set()

    @classmethod
    def _cache_entry(cls, username: str, password: str, stored: str) -> bytes:
        message = "\0".join((username, password, stored)).encode("utf-8")
        return hmac.new(cls._cache_key, message, hashlib.sha256).digest()

    @classmethod
    def check(cls, username: str, password: str) -> bool:
        with cls.sema:
            stored = cls.users.get(username)
            if stored is None:
                return False
            entry = cls._cache_entry(username, password, stored)
            if entry in cls._verified:
                return True

        if not verify_password(password=password, stored=stored):
            return False
        with cls.sema:
            cls._verified.add(entry)
        return True

    @classmethod
    def create_default_file_if_not_exist(cls) -> Optional[str]:
        """Create users.json with the user admin and a random password.

        Returns the password if the file was created, otherwise None.
        """
        if cls.path and not cls.path.exists():
            password = secrets.token_urlsafe(9)
            _write_users(
                path=cls.path,
                users=[{"username": "admin", "password": hash_password(password)}],
            )
            logging.info(f"File {str(cls.path)} created with user admin")
            print(f"File {str(cls.path)} created")
            print(f"  Username: admin, password: {password}")
            print("  Please note the password, it is not displayed again.", flush=True)
            return password
        return None

    @classmethod
    def update(cls, path: Optional[pathlib.Path] = None) -> None:
        if path:
            cls.path = path

        if cls.path:
            cls.create_default_file_if_not_exist()

            with open(cls.path) as f:
                data = json.load(f)
            jsonschema.validate(instance=data, schema=SCHEMA)

            # replace plain text passwords by their hashes
            if not all(is_hashed(user["password"]) for user in data):
                for user in data:
                    if not is_hashed(user["password"]):
                        user["password"] = hash_password(user["password"])
                _write_users(path=cls.path, users=data)
                logging.info(f"Passwords in {str(cls.path)} replaced by hashes")

            with cls.sema:
                cls.users = {}
                cls._verified = set()
                for user in data:
                    cls.users[user["username"]] = user["password"]


class LoginThrottle:
    """Slow down guessing of passwords.

    After MAX_FAILURES failed logins of an address within FAILURE_WINDOW seconds,
    further logins of this address are rejected for LOCK_TIME seconds.
    """

    MAX_FAILURES = 5
    FAILURE_WINDOW = 60
    LOCK_TIME = 60

    sema = threading.Semaphore()
    # address -> times of the failed logins
    failures: dict[str, list[float]] = {}
    # address -> end of the lock time
    locked_until: dict[str, float] = {}

    @classmethod
    def is_locked(cls, address: str, now: Optional[float] = None) -> bool:
        now = time.monotonic() if now is None else now
        with cls.sema:
            until = cls.locked_until.get(address)
            if until is None:
                return False
            if now >= until:
                del cls.locked_until[address]
                return False
            return True

    @classmethod
    def add_failure(cls, address: str, now: Optional[float] = None) -> None:
        now = time.monotonic() if now is None else now
        with cls.sema:
            times = [
                t for t in cls.failures.get(address, []) if now - t < cls.FAILURE_WINDOW
            ]
            times.append(now)
            if len(times) >= cls.MAX_FAILURES:
                cls.locked_until[address] = now + cls.LOCK_TIME
                times = []
            if times:
                cls.failures[address] = times
            else:
                cls.failures.pop(address, None)

    @classmethod
    def reset(cls, address: str) -> None:
        with cls.sema:
            cls.failures.pop(address, None)
            cls.locked_until.pop(address, None)
