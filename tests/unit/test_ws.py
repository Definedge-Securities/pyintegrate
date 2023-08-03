###############################################################################
# MIT License                                                                 #
###############################################################################
# Copyright (c) 2023 Definedge Securities Broking Pvt. Ltd.                   #
###############################################################################
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the "Software"),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
###############################################################################

from base64 import b64encode
from hashlib import sha256
from unittest.mock import Mock

from autobahn.websocket.protocol import WebSocketProtocol  # type: ignore
from autobahn.websocket.types import ConnectingRequest  # type: ignore

from integrate.ws import IntegrateWebSocketClientProtocol


def tearDown(iwsproto: IntegrateWebSocketClientProtocol) -> None:
    """
    Tear down the connection.

    :param iwsproto: IntegrateWebSocketClientProtocol object
    :type iwsproto: IntegrateWebSocketClientProtocol
    :return: None
    """
    for call in [  # type: ignore
        iwsproto.autoPingPendingCall,  # type: ignore
        iwsproto.autoPingTimeoutCall,  # type: ignore
        iwsproto.openHandshakeTimeoutCall,
        iwsproto.closeHandshakeTimeoutCall,  # type: ignore
    ]:
        if call is not None:
            call.cancel()  # type: ignore


def test_auto_ping(iwsproto: IntegrateWebSocketClientProtocol) -> None:
    """
    Test auto ping.

    :param iwsproto: IntegrateWebSocketClientProtocol object
    :type iwsproto: IntegrateWebSocketClientProtocol
    :return: None
    """
    iwsproto.autoPingInterval = 1  # type: ignore
    iwsproto.websocket_protocols = [Mock()]  # type: ignore
    iwsproto.websocket_extensions = []  # type: ignore
    iwsproto._onOpen = lambda: None  # type: ignore
    iwsproto._wskey = '0' * 24  # type: ignore
    iwsproto.peer = Mock()

    # usually provided by the Twisted or asyncio specific
    # subclass, but we're testing the parent here...
    iwsproto._onConnect = Mock()  # type: ignore
    iwsproto._closeConnection = Mock()  # type: ignore

    # start the handshake
    iwsproto.startHandshake()

    # set up a connection
    iwsproto._actuallyStartHandshake(  # type: ignore
        ConnectingRequest(
            host="example.com",
            port=80,
            resource="/ws",
        )
    )

    key: bytes = iwsproto.websocket_key + WebSocketProtocol._WS_MAGIC  # type: ignore
    iwsproto.data = (
        b"HTTP/1.1 101 Switching Protocols\x0d\x0a"
        b"Upgrade: websocket\x0d\x0a"
        b"Connection: upgrade\x0d\x0a"
        b"Sec-Websocket-Accept: "
        + b64encode(sha256(key).digest())
        + b"\x0d\x0a\x0d\x0a"
    )
    iwsproto.processHandshake()

    # Assert that the auto ping is set
    assert iwsproto.autoPingPendingCall is not None  # type: ignore
