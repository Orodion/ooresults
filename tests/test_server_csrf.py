# Copyright (C) 2026 Rainer Garus
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


from typing import Optional

import pytest

from ooresults._server import request_allowed


@pytest.mark.parametrize("method", ["GET", "HEAD", "OPTIONS", "get"])
def test_safe_methods_are_allowed_without_header(method: str) -> None:
    assert request_allowed(
        method=method,
        requested_with=None,
        origin="https://evil.example.com",
        host="localhost:8080",
    )


@pytest.mark.parametrize("requested_with", [None, "", "fetch"])
def test_post_without_csrf_header_is_rejected(requested_with: Optional[str]) -> None:
    assert not request_allowed(
        method="POST",
        requested_with=requested_with,
        origin=None,
        host="localhost:8080",
    )


def test_post_with_csrf_header_and_without_origin_is_allowed() -> None:
    assert request_allowed(
        method="POST",
        requested_with="XMLHttpRequest",
        origin=None,
        host="localhost:8080",
    )


def test_post_with_csrf_header_and_same_origin_is_allowed() -> None:
    assert request_allowed(
        method="POST",
        requested_with="XMLHttpRequest",
        origin="https://localhost:8080",
        host="localhost:8080",
    )


@pytest.mark.parametrize(
    "origin, host",
    [
        ("https://evil.example.com", "localhost:8080"),
        ("https://localhost:8443", "localhost:8080"),
        ("null", "localhost:8080"),
        ("https://localhost:8080", None),
    ],
)
def test_post_with_foreign_origin_is_rejected(origin: str, host: Optional[str]) -> None:
    assert not request_allowed(
        method="POST",
        requested_with="XMLHttpRequest",
        origin=origin,
        host=host,
    )
