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


import json
import pathlib
import stat
import sys

import pytest

from ooresults import user
from ooresults.user import LoginThrottle
from ooresults.user import Users
from ooresults.user import hash_password
from ooresults.user import is_hashed
from ooresults.user import verify_password


@pytest.fixture(autouse=True)
def reset_users() -> None:
    Users.path = None
    Users.users = {}
    Users._verified = set()
    LoginThrottle.failures = {}
    LoginThrottle.locked_until = {}


def test_default_file_has_user_admin_with_random_password(
    tmp_path: pathlib.Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "users.json"

    Users.update(path=path)
    assert path.exists()

    with open(path) as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["username"] == "admin"
    assert is_hashed(data[0]["password"])
    assert not Users.check("admin", "admin")
    assert Users.path == path

    # the password is displayed on the console
    out = capsys.readouterr().out
    password = out.split("password: ")[1].split()[0]
    assert Users.check("admin", password)


def test_default_passwords_are_different(tmp_path: pathlib.Path) -> None:
    Users.path = tmp_path / "a.json"
    password_1 = Users.create_default_file_if_not_exist()
    Users.path = tmp_path / "b.json"
    password_2 = Users.create_default_file_if_not_exist()
    assert password_1 is not None
    assert password_1 != password_2


def test_existing_file_is_not_overwritten(tmp_path: pathlib.Path) -> None:
    path = tmp_path / "users.json"
    path.write_text("[]")
    Users.path = path
    assert Users.create_default_file_if_not_exist() is None
    assert path.read_text() == "[]"


def test_plain_text_passwords_are_replaced_by_hashes(tmp_path: pathlib.Path) -> None:
    users = [
        {"username": "a", "password": "x"},
        {"username": "b", "password": "y"},
        {"username": "c", "password": "z"},
    ]
    path = tmp_path / "users.json"
    path.write_text(json.dumps(users))

    Users.update(path=path)

    with open(path) as f:
        data = json.load(f)
    assert [u["username"] for u in data] == ["a", "b", "c"]
    assert all(is_hashed(u["password"]) for u in data)
    assert Users.check("a", "x")
    assert Users.check("b", "y")
    assert Users.check("c", "z")
    assert not Users.check("a", "y")


def test_hashed_passwords_are_kept(tmp_path: pathlib.Path) -> None:
    users = [{"username": "a", "password": hash_password("x")}]
    path = tmp_path / "users.json"
    path.write_text(json.dumps(users))
    mtime = path.stat().st_mtime_ns

    Users.update(path=path)

    assert path.stat().st_mtime_ns == mtime
    assert Users.check("a", "x")


@pytest.mark.skipif(sys.platform == "win32", reason="file modes not supported")
def test_written_file_is_only_readable_by_the_owner(tmp_path: pathlib.Path) -> None:
    path = tmp_path / "users.json"
    Users.update(path=path)
    assert stat.S_IMODE(path.stat().st_mode) == 0o600


def test_check_username_and_password() -> None:
    Users.users = {
        "abc": hash_password("p1"),
        "def": hash_password("p2"),
        "ghi": "p3",
    }
    assert Users.check("abc", "p1")
    assert Users.check("def", "p2")
    assert Users.check("ghi", "p3")
    assert not Users.check("abc", "p2")
    assert not Users.check("abc", "p3")
    assert not Users.check("xxx", "pp")
    # checked twice, the second time with the cache
    assert Users.check("abc", "p1")
    assert not Users.check("abc", "p2")


def test_hash_contains_salt() -> None:
    h1 = hash_password("secret")
    h2 = hash_password("secret")
    assert h1 != h2
    assert verify_password("secret", h1)
    assert verify_password("secret", h2)
    assert not verify_password("Secret", h1)


def test_invalid_hash_is_rejected() -> None:
    assert not verify_password("secret", "scrypt$16384$8$1$!!!$!!!")


def test_address_is_locked_after_too_many_failures() -> None:
    for i in range(LoginThrottle.MAX_FAILURES - 1):
        LoginThrottle.add_failure("1.2.3.4", now=100.0 + i)
        assert not LoginThrottle.is_locked("1.2.3.4", now=100.0 + i)

    LoginThrottle.add_failure("1.2.3.4", now=110.0)
    assert LoginThrottle.is_locked("1.2.3.4", now=110.0)
    assert not LoginThrottle.is_locked("5.6.7.8", now=110.0)

    # the lock ends after LOCK_TIME seconds
    assert LoginThrottle.is_locked("1.2.3.4", now=110.0 + LoginThrottle.LOCK_TIME - 1)
    assert not LoginThrottle.is_locked("1.2.3.4", now=110.0 + LoginThrottle.LOCK_TIME)


def test_old_failures_are_forgotten() -> None:
    for i in range(LoginThrottle.MAX_FAILURES - 1):
        LoginThrottle.add_failure("1.2.3.4", now=100.0)
    LoginThrottle.add_failure("1.2.3.4", now=100.0 + LoginThrottle.FAILURE_WINDOW)
    assert not LoginThrottle.is_locked(
        "1.2.3.4", now=100.0 + LoginThrottle.FAILURE_WINDOW
    )


def test_reset_removes_failures() -> None:
    for i in range(LoginThrottle.MAX_FAILURES - 1):
        LoginThrottle.add_failure("1.2.3.4", now=100.0)
    LoginThrottle.reset("1.2.3.4")
    LoginThrottle.add_failure("1.2.3.4", now=101.0)
    assert not LoginThrottle.is_locked("1.2.3.4", now=101.0)


def test_module_exports() -> None:
    assert user.SCRYPT_N >= 2**14
