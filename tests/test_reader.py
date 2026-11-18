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


import json
import threading
import time
from unittest import mock

import websocket

from ooresults._reader import WebSocketClient


def test_receive_returns_answer() -> None:
    client = WebSocketClient()
    client.opened = True
    client.queue.put(json.dumps({"status": "OK"}))

    assert client.receive(timeout=1) == {"status": "OK"}


def test_receive_returns_empty_dict_if_not_connected() -> None:
    client = WebSocketClient()
    client.opened = False

    assert client.receive(timeout=1) == {}


def test_receive_returns_empty_dict_after_timeout() -> None:
    client = WebSocketClient()
    client.opened = True

    start = time.monotonic()
    assert client.receive(timeout=0.1) == {}
    assert time.monotonic() - start < 5


def test_closing_the_connection_wakes_up_a_waiting_receiver() -> None:
    client = WebSocketClient()
    client.opened = True
    result: list[dict] = []

    receiver = threading.Thread(target=lambda: result.append(client.receive(60)))
    receiver.start()
    time.sleep(0.1)
    client.on_close(wsapp=None, close_status_code=None, close_msg=None)
    receiver.join(timeout=5)

    assert not receiver.is_alive()
    assert result == [{}]
    assert client.opened is False


def test_closing_an_unopened_connection_does_not_fill_the_queue() -> None:
    client = WebSocketClient()
    client.opened = False

    client.on_close(wsapp=None, close_status_code=None, close_msg=None)
    assert client.queue.empty()


def test_send_catches_websocket_exceptions() -> None:
    client = WebSocketClient()
    client.opened = True
    client.ws = mock.Mock()
    client.ws.send.side_effect = websocket.WebSocketConnectionClosedException(
        "socket is already closed."
    )

    assert client.send_and_receive(item={"entryType": "cardRead"}, timeout=0.1) == {}
