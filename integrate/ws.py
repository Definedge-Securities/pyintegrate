# -*- coding: utf-8 -*-
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

"""
This module contains the IntegrateWebSocket class which is used to
connect to the Integrate WebSocket API and subscribe to ticks, order
updates and bid-ask depth updates.

Example:

.. code-block:: python

    from integrate import ConnectToIntegrate, IntegrateWebSocket

    # Create a ConnectToIntegrate object
    c2i = ConnectToIntegrate()

    # Login to Integrate
    c2i.login(api_token="YOUR_API_TOKEN", api_secret="YOUR_API_SECRET")

    # Create an IntegrateWebSocket object
    iws = IntegrateWebSocket(c2i)

    # Connect to Integrate WebSocket server
    iws.connect()

    # Check if WebSocket connection is established
    iws.is_connected()

    # Subscribe to ticks
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_TICK)

    # Subscribe to order updates
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_ORDER)

    # Subscribe to bid-ask depth updates
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_DEPTH)

    # Unsubscribe from ticks
    iws.unsubscribe(iws.c2i.SUBSCRIPTION_TYPE_TICK)

    # Unsubscribe from order updates
    iws.unsubscribe(iws.c2i.SUBSCRIPTION_TYPE_ORDER)

    # Unsubscribe from bid-ask depth updates
    iws.unsubscribe(iws.c2i.SUBSCRIPTION_TYPE_DEPTH)

    # Resubscribe to all current subscribed tokens
    iws.resubscribe()

    # Stop reconnecting
    iws.stop_retry()

    # Stop the event loop
    iws.stop()
"""

from __future__ import annotations

from json import dumps, loads
from logging import Logger, getLogger
from threading import Thread
from typing import Any, Union

from autobahn.twisted.websocket import connectWS  # type: ignore
from autobahn.twisted.websocket import (  # type: ignore
    ConnectionResponse,
    WebSocketClientFactory,
    WebSocketClientProtocol,
)
from twisted.internet.base import BaseConnector
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.internet.ssl import optionsForClientTLS  # type: ignore
from twisted.python.failure import Failure
from twisted.python.log import PythonLoggingObserver

from integrate import ConnectToIntegrate

log: Logger = getLogger(__name__)
observer = PythonLoggingObserver(loggerName=__name__)


class IntegrateWebSocketClientProtocol(WebSocketClientProtocol):
    """
    Definedge Securities Integrate autobahn WebSocket protocol to specify the behavior of the client.

    :reference:

    - `Autobahn WebSocketClientProtocol Class <https://autobahn.readthedocs.io/en/latest/reference/autobahn.twisted.html#autobahn.twisted.websocket.WebSocketClientProtocol>`_
    - `Autobahn Connection Lifecycle <https://autobahn.readthedocs.io/en/latest/websocket/programming.html#connection-lifecycle>`_
    - `WebSocketClient Example <https://github.com/crossbario/autobahn-python/blob/master/examples/twisted/websocket/echo/client.py>`_
    """

    factory: IntegrateWebSocketClientFactory

    def onConnect(self, response: ConnectionResponse) -> None:
        """
        Callback fired during WebSocket opening handshake when a client connects to a server.

        :param `response`: The connection response.
        :type `response`: `ConnectionResponse`
        :returns: `None`
        """
        log.debug(
            f"Server connected: {response.headers}\n{response.extensions}\n{response.peer}\n{response.protocol}"
        ) if self.factory.logging else None
        # Hand off to custom factory callback
        self.factory.on_connect(self, response)

    def onOpen(self) -> None:
        """
        Callback fired when the initial WebSocket opening handshake was completed.

        :returns: `None`
        """
        # Hand off to custom factory callback
        self.factory.on_open()

    def onMessage(self, payload: bytes, isBinary: bool) -> None:
        """
        Callback fired when a complete WebSocket message was received.

        :param `payload`: The WebSocket message received.
        :param `isBinary`: Flag indicating whether payload is binary or UTF-8 encoded text.
        :type `payload`: `bytes`
        :type `isBinary`: `bool`
        :returns: `None`
        """
        # Hand off to custom factory callback
        self.factory.on_message(payload, isBinary)

    def onClose(self, wasClean: bool, code: int, reason: str) -> None:
        """
        Callback fired when the WebSocket connection has been closed.

        :param `wasClean`: Flag indicating whether the connection was closed cleanly or not.
        :param `code`: Close status code.
        :param `reason`: Close reason.
        :type `wasClean`: `bool`
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        :note: `RFC6455 <https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1>`_ defines the status codes on connection close
        """
        # Hand off to custom factory callbacks
        self.factory.on_error(code, reason) if not wasClean else None
        self.factory.on_close(code, reason)


class IntegrateWebSocketClientFactory(
    WebSocketClientFactory, ReconnectingClientFactory
):
    """
    Definedge Securities Integrate autobahn WebSocket client factory to implement auto reconnection.

    :param `reconnect`: Flag indicating whether to reconnect on connection lost.
    :type `reconnect`: `bool`
    :returns: `None`

    Auto reconnection is enabled by default and it can be disabled by passing :py:attr:`IntegrateWebSocket.reconnect` = False in :py:meth:`IntegrateWebSocket.connect`.
    Reconnection cannot happen if the event loop is terminated using :py:meth:`IntegrateWebSocket.stop` method inside :py:meth:`IntegrateWebSocket.on_close` callback.

    Auto reconnection is based on `Exponential backoff algorithm <https://en.wikipedia.org/wiki/Exponential_backoff>`_ in which
    next retry delay will be increased exponentially. :py:attr:`IntegrateWebSocket.reconnect_max_delay` and :py:attr:`IntegrateWebSocket.reconnect_max_tries` params can be used to tweak
    the algorithm where:
    - `reconnect_max_delay` is the maximum delay after which subsequent reconnection delay will become constant and
    - `reconnect_max_tries` is maximum number of retries before it quits reconnection.

    For example if `reconnect_max_delay` is 60 seconds and `reconnect_max_tries` is 30 then the first reconnection delay starts from
    minimum delay which is 2 seconds and keep increasing up to 60 seconds after which it becomes constant and when reconnection attempt
    is reached upto 30 then it stops reconnecting.

    - :py:meth:`IntegrateWebSocket.stop_retry` can be used to stop ongoing reconnect attempts
    - :py:meth:`IntegrateWebSocket.on_reconnection` callback will be called with current reconnect attempt
    - :py:meth:`IntegrateWebSocket.on_stop_reconnection` is called when reconnection attempts reaches max retries.

    :reference:

    - `Autobahn WebSocketClientFactory <https://autobahn.readthedocs.io/en/latest/websocket/reference.html#autobahn.twisted.websocket.WebSocketClientFactory>`_
    - `Reconnecting WebSocketClientFactory Example <https://github.com/crossbario/autobahn-python/blob/master/examples/twisted/websocket/reconnecting/client.py>`_
    """

    logging: bool = False
    is_reconnection: bool = False
    protocol = IntegrateWebSocketClientProtocol

    def __init__(self, *args, **kwargs) -> None:  # type: ignore
        # Pop out reconnect flag from kwargs as it is not a valid argument for WebSocketClientFactory
        self._reconnect: bool = kwargs.pop("reconnect", True)  # type: ignore
        super(IntegrateWebSocketClientFactory, self).__init__(*args, **kwargs)  # type: ignore

    def startedConnecting(self, connector: BaseConnector) -> None:
        """
        Called when a connection has been started. Stop trying to connect to server if maxRetries have been made.

        :param `connector`: The connector that has started.
        :type `connector`: `BaseConnector`
        :returns: `None`
        """
        if self.retries and self.maxRetries and self.retries > self.maxRetries:
            log.debug(
                f"Maximum retries ({self.maxRetries}) exhausted."
            ) if self.logging else None
            # Stop the loop for exceeding max retry attempts
            self.stopTrying()
            self.on_stop_reconnection()

    def clientConnectionFailed(
        self, connector: BaseConnector, reason: Failure
    ) -> None:
        """
        Called when a connection has failed to connect.

        :param `connector`: The connector that has failed.
        :param `reason`: The reason for the failure.
        :type `connector`: `BaseConnector`
        :type `reason`: `Failure`
        :returns: `None`
        """
        if self.retries and self.retries > 0:
            log.error(
                f"Retrying connection... Retry attempt: {self.retries}. Next retry in: {int(round(self.delay))} seconds"
            ) if self.logging else None
            self.is_reconnection = True
            # on reconnect callback
            self.on_reconnection(self.retries)
            # Retry the connection
            self.retry(connector)  # type: ignore

    def clientConnectionLost(self, connector: BaseConnector, reason: Failure) -> None:  # type: ignore
        """
        Called when an established connection is lost.

        :param `connector`: The connector that has lost connection.
        :param `reason`: The reason for the lost connection.
        :type `connector`: `BaseConnector`
        :type `reason`: `Failure`
        :returns: `None`
        """
        if self.retries and self.retries > 0:
            log.error(
                f"Retrying connection... Retry attempt: {self.retries}. Next retry in: {int(round(self.delay))} seconds"
            ) if self.logging else None
            self.is_reconnection = True
            # on reconnect callback
            self.on_reconnection(self.retries)
            # Retry the connection
            self.retry(connector)  # type: ignore

    def on_connect(
        self,
        protocol: IntegrateWebSocketClientProtocol,
        response: ConnectionResponse,
    ) -> None:
        """
        Callback stub for IntegrateWebSocket after onConnect.

        :param `protocol`: The WebSocket protocol instance.
        :param `response`: The HTTP response.
        :type `protocol`: `IntegrateWebSocketClientProtocol`
        :type `response`: `ConnectionResponse`
        :returns: `None`
        """
        pass

    def on_open(self) -> None:
        """
        Callback stub for IntegrateWebSocket after onOpen.

        :returns: `None`
        """
        pass

    def on_close(self, code: int, reason: str) -> None:
        """
        Callback stub for IntegrateWebSocket after onClose.

        :param `code`: Close status code.
        :param `reason`: Close reason.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        """
        pass

    def on_message(
        self,
        payload: bytes,
        is_binary: bool,
    ) -> None:
        """
        Callback stub for IntegrateWebSocket after onMessage.

        :param `payload`: The WebSocket message payload.
        :param `is_binary`: Flag indicating whether the payload is binary or not.
        :type `payload`: `bytes`
        :type `is_binary`: `bool`
        :returns: `None`
        """
        pass

    def on_error(self, code: int, reason: str) -> None:
        """
        Callback stub for IntegrateWebSocket when an error occurs.

        :param `code`: Close status code.
        :param `reason`: Close reason.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        """
        pass

    def on_reconnection(self, retries: int) -> None:
        """
        Callback stub for IntegrateWebSocket on reconnection.

        :param `retries`: The number of retries made.
        :type `retries`: `int`
        :returns: `None`
        """
        pass

    def on_stop_reconnection(self) -> None:
        """
        Callback stub for IntegrateWebSocket if maxRetries have been made.

        :returns: `None`
        """
        pass


class IntegrateWebSocket:
    """
    WebSocket client for interacting with Definedge Securities' streaming quotes, order and depth updates.

    :param `connect_to_integrate`: The connection object.
    :param `logging`: Enable or disable logging. Defaults to `False`.
    :type `connect_to_integrate`: `ConnectToIntegrate`
    :type `logging`: `bool`

    Callbacks
    ---------

    - :py:meth:`IntegrateWebSocket.on_connect`: Called when a connection has been established.
    - :py:meth:`IntegrateWebSocket.on_open`: Called when the initial WebSocket opening handshake was completed.
    - :py:meth:`IntegrateWebSocket.on_login`: Called when the login is successful.
    - :py:meth:`IntegrateWebSocket.on_close`: Called when the WebSocket connection has been closed.
    - :py:meth:`IntegrateWebSocket.on_error`: Called when an error occurs.
    - :py:meth:`IntegrateWebSocket.on_reconnection`: Called when a reconnection attempt is made.
    - :py:meth:`IntegrateWebSocket.on_stop_reconnection`: Called when maxRetries have been made.
    - :py:meth:`IntegrateWebSocket.on_exception`: Called when a Python exception occurs.
    - :py:meth:`IntegrateWebSocket.on_tick_update`: Called when a tick is received.
    - :py:meth:`IntegrateWebSocket.on_order_update`: Called when an order update is received.
    - :py:meth:`IntegrateWebSocket.on_depth_update`: Called when a bid-ask depth update is received.
    - :py:meth:`IntegrateWebSocket.on_acknowledgement`: Called when an request acknowledgement is received.
    """

    # Default values
    _auto_ping_interval = 10
    _auto_ping_timeout = 5
    _min_reconnect_max_delay = 5
    _max_reconnect_max_tries = 300

    def __init__(
        self,
        connect_to_integrate: ConnectToIntegrate,
        logging: bool = False,
    ) -> None:
        # Initialize properties
        self.c2i: ConnectToIntegrate = connect_to_integrate
        self.subscriptions: dict[str, set[str]] = {
            self.c2i.SUBSCRIPTION_TYPE_TICK: set(),
            self.c2i.SUBSCRIPTION_TYPE_ORDER: set(),
            self.c2i.SUBSCRIPTION_TYPE_DEPTH: set(),
        }
        self.is_logged_in: bool = False

        self._socket_url: str = (
            "wss://trade.definedgesecurities.com/NorenWSTRTP/"
        )
        self._logging: bool = logging
        observer.start() if self._logging else None

    def connect(
        self,
        socket_url: str | None = None,
        daemonize: bool = False,
        reconnect: bool = True,
        reconnect_max_tries: int = 30,
        reconnect_max_delay: int = 60,
        connect_timeout: int = 30,
        ssl_verify: bool = True,
        proxy: dict[str, str] | None = None,
    ) -> None:
        """
        Establish a websocket connection with Definedge Securities Integrate.

        :param `socket_url`: The websocket URL to connect to. Defaults to `wss://trade.definedgesecurities.com/NorenWSTRTP/`.
        :param `daemonize`: Indicates if the client should run a daemon. Defaults to `False`.
        :param `reconnect`: Indicates if the client should auto reconnect. Defaults to `True`.
        :param `reconnect_max_tries`: Maximum number of retries before it stops reconnecting. Defaults to 30.
        :param `reconnect_max_delay`: Maximum delay after which subsequent reconnection delay will become constant. Defaults to 60.
        :param `connect_timeout`: Maximum time (seconds) for which the API client will wait for a request to complete before it fails. Defaults to 30 seconds.
        :param `ssl_verify`: Enable or disable SSL verification. Defaults to `True`.
        :param `proxy`: Proxy URL. Defaults to `None`.
        :type `socket_url`: `str`
        :type `daemonize`: `bool`
        :type `reconnect`: `bool`
        :type `reconnect_max_tries`: `int`
        :type `reconnect_max_delay`: `int`
        :type `connect_timeout`: `int`
        :type `ssl_verify`: `bool`
        :type `proxy`: `dict[str, str]`
        """
        # Initialize properties
        self._reconnect_max_tries: int = (
            self._max_reconnect_max_tries
            if reconnect_max_tries > self._max_reconnect_max_tries
            else reconnect_max_tries
        )
        self._reconnect_max_delay: int = (
            self._min_reconnect_max_delay
            if reconnect_max_delay < self._min_reconnect_max_delay
            else reconnect_max_delay
        )
        self._connect_timeout: int = connect_timeout
        self._socket_url = socket_url if socket_url else self._socket_url
        self._protocol: IntegrateWebSocketClientProtocol | None = None

        # Initialize IntegrateWebSocketClientFactory
        self._factory = IntegrateWebSocketClientFactory(
            self._socket_url,
            proxy=proxy,
            reconnect=reconnect,
        )
        self._factory.protocol = IntegrateWebSocketClientProtocol
        self._factory.logging = self._logging
        self._factory.maxDelay = self._reconnect_max_delay
        self._factory.maxRetries = self._reconnect_max_tries  # type: ignore

        # Register callbacks
        self._factory.on_connect = self._on_connect  # type: ignore
        self._factory.on_open = self._on_open  # type: ignore
        self._factory.on_error = self._on_error  # type: ignore
        self._factory.on_close = self._on_close  # type: ignore
        self._factory.on_message = self._on_message  # type: ignore
        self._factory.on_reconnection = self._on_reconnection  # type: ignore
        self._factory.on_stop_reconnection = self._on_stop_reconnection  # type: ignore

        # Set auto ping with interval and timeout
        self._factory.setProtocolOptions(  # type: ignore
            autoPingInterval=self._auto_ping_interval,
            autoPingTimeout=self._auto_ping_timeout,
            serverConnectionDropTimeout=10,
            closeHandshakeTimeout=10,
        )

        # Establish WebSocket connection to the server
        opts: dict[str, Any] = {}
        opts["factory"] = self._factory
        if ssl_verify:
            opts["contextFactory"] = optionsForClientTLS(self._factory.host)  # type: ignore
        opts["timeout"] = self._connect_timeout
        self._connector: BaseConnector = connectWS(**opts)

        try:
            # Run when reactor is not running
            if not self._connector.state == "disconnected":  # type: ignore
                if daemonize:
                    # Signals are not allowed in non main thread by twisted so suppress it.
                    Thread(target=self._connector.reactor.run, daemon=True, kwargs={"installSignalHandlers": False}).start()  # type: ignore
                else:
                    self._connector.reactor.run()  # type: ignore
        except Exception as e:
            self._on_exception(e)

    def is_connected(self) -> bool:
        """
        Check if WebSocket connection is established.

        :returns: `True` if connection is established, else `False`.
        """
        return (
            True
            if self._protocol
            and self._protocol.state == self._protocol.STATE_OPEN
            else False
        )

    def login(self) -> None:
        """
        Login to Definedge Securities Integrate.

        :returns: `None`
        """
        if self.is_connected():
            self._protocol.sendMessage(  # type: ignore
                dumps(
                    {
                        "t": "c",
                        "uid": self.c2i.uid,
                        "actid": self.c2i.actid,
                        "source": "TRTP",
                        "susertoken": self.c2i.ws_session_key,
                    },
                    ensure_ascii=False,
                ).encode('utf-8')
            )
        else:
            self._on_exception(
                Exception(
                    f"Not connected to Definedge Securities Integrate WebSocket server: {self._protocol.state if self._protocol else None}"
                )
            )

    def subscribe(
        self,
        subscription_type: str,
        tokens: list[tuple[str, str]] | None = None,
    ) -> None:
        """
        Subscribe to a list of security tokens.

        :param `subscription_type`: The subscription type. Valid values are `TICK`, `ORDER` and `DEPTH`.
        :param `tokens`: List of security tokens to subscribe to. Defaults to `None`.
        :type `subscription_type`: `str`
        :type `tokens`: `list[tuple[str, str]]`
        :returns: `None`
        """
        self.check_token_validity(tokens) if tokens else None
        t: str = ""
        if subscription_type == self.c2i.SUBSCRIPTION_TYPE_TICK:
            t = "t"
        elif subscription_type == self.c2i.SUBSCRIPTION_TYPE_ORDER:
            t = "o"
        elif subscription_type == self.c2i.SUBSCRIPTION_TYPE_DEPTH:
            t = "d"
        else:
            self._on_exception(
                ValueError(f"Invalid subscription type: {subscription_type}")
            )

        try:
            if (
                subscription_type == self.c2i.SUBSCRIPTION_TYPE_TICK
                or subscription_type == self.c2i.SUBSCRIPTION_TYPE_DEPTH
            ) and tokens:
                for token in tokens:
                    self.subscriptions[subscription_type].add("|".join(token))
                self._protocol.sendMessage(dumps({"t": t, "k": "#".join(self.subscriptions[subscription_type])}, ensure_ascii=False).encode('utf-8'))  # type: ignore
            else:
                self.subscriptions[subscription_type].add(self.c2i.actid)
                self._protocol.sendMessage(dumps({"t": t, "actid": self.c2i.actid}, ensure_ascii=False).encode('utf-8'))  # type: ignore
        except Exception as e:
            self._on_exception(
                Exception(
                    f"Error subscribing tokens for {subscription_type}: {e}"
                )
            )

    def unsubscribe(
        self,
        unsubscription_type: str,
        tokens: list[tuple[str, str]] | None = None,
    ) -> None:
        """
        Unsubscribe the given list of security tokens.

        :param `unsubscription_type`: The unsubscription type. Valid values are `TICK`, `ORDER` and `DEPTH`.
        :param `tokens`: List of security tokens to unsubscribe from. Defaults to `None`.
        :type `unsubscription_type`: `str`
        :type `tokens`: `list[tuple[str, str]]`
        :returns: `None`
        """
        self.check_token_validity(tokens) if tokens else None
        t: str = ""
        if unsubscription_type == self.c2i.SUBSCRIPTION_TYPE_TICK:
            t = "u"
        elif unsubscription_type == self.c2i.SUBSCRIPTION_TYPE_ORDER:
            t = "uo"
        elif unsubscription_type == self.c2i.SUBSCRIPTION_TYPE_DEPTH:
            t = "ud"
        else:
            self._on_exception(
                ValueError(
                    f"Invalid unsubscription type: {unsubscription_type}"
                )
            )

        try:
            if (
                unsubscription_type == self.c2i.SUBSCRIPTION_TYPE_TICK
                or unsubscription_type == self.c2i.SUBSCRIPTION_TYPE_DEPTH
            ) and tokens:
                self._protocol.sendMessage(dumps({"t": t, "k": "#".join(tokens)}, ensure_ascii=False).encode('utf-8'))  # type: ignore
                for token in tokens:
                    self.subscriptions[unsubscription_type].remove(
                        "|".join(token)
                    )
            else:
                self._protocol.sendMessage(dumps({"t": t, "actid": self.c2i.actid}, ensure_ascii=False).encode('utf-8'))  # type: ignore
                self.subscriptions[unsubscription_type].remove(self.c2i.actid)
        except Exception as e:
            self._on_exception(
                Exception(
                    f"Error unsubscribing tokens for {unsubscription_type}: {e}"
                )
            )

    def resubscribe(self) -> None:
        """
        Resubscribe to all current subscribed tokens.

        :returns: `None`
        """
        for subscription_type in self.subscriptions.keys():
            if subscription_type == self.c2i.SUBSCRIPTION_TYPE_ORDER:
                self.subscribe(self.c2i.SUBSCRIPTION_TYPE_ORDER)
            else:
                self.subscribe(
                    subscription_type,
                    [
                        tuple(token.split("|"))  # type: ignore
                        for token in self.subscriptions[subscription_type]
                    ],
                )

    def check_token_validity(self, tokens: list[tuple[str, str]]) -> None:
        """
        Check if the given list of security tokens are valid.

        :param `tokens`: List of security tokens to check.
        :type `tokens`: `list[tuple[str, str]]`
        :returns: `None`
        """
        for exchange, token in tokens:
            if exchange not in self.c2i.exchange_types:
                self._on_exception(
                    ValueError(f"Invalid exchange type: {exchange}")
                )

            t: Union[str, None] = next(
                (
                    i["token"]
                    for i in self.c2i.symbols
                    if i["segment"] == exchange and i["token"] == token
                ),
                None,
            )
            if not t:
                self._on_exception(
                    Exception(
                        f"{token} in {exchange} not found in symbols file"
                    )
                )

    def close(
        self, code: int | None = None, reason: str | None = None
    ) -> None:
        """
        Close the WebSocket connection.

        :param `code`: The close code. Defaults to `None`.
        :param `reason`: The close reason. Defaults to `None`.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        """
        self.stop_retry()
        self._close(code, reason)

    def close_on_exception(self, reason: str | None = None) -> None:
        """
        Close the WebSocket connection on exception.

        :param `reason`: The close reason. Defaults to `None`.
        :type `reason`: `str`
        :returns: `None`
        """
        self.close(1000, reason)

    def stop(self) -> None:
        """
        Stop the event loop.

        :returns: `None`
        :note: Should be used if main thread has to be closed in `on_close` method. Reconnection cannot happen after this method is used.
        """
        self.close(1000, "Client stopped")
        self._connector.reactor.callFromThread(
            self._connector.reactor.stop
        ) if self._connector.reactor.running else None

    def stop_retry(self) -> None:
        """
        Stop auto retry when it is in progress.

        :returns: `None`
        """
        self._factory.stopTrying() if self._factory else None

    def on_connect(
        self, iws: IntegrateWebSocket, response: ConnectionResponse
    ) -> None:
        """
        Callback function called when the WebSocket connection is established.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `response`: The `ConnectionResponse` instance.
        :type `iws`: `IntegrateWebSocket`
        :type `response`: `ConnectionResponse`
        :returns: `None`
        """
        pass

    def on_open(self, iws: IntegrateWebSocket) -> None:
        """
        Callback function called when the WebSocket connection is opened.

        :param `iws`: The `IntegrateWebSocket` instance.
        :type `iws`: `IntegrateWebSocket`
        :returns: `None`
        """
        pass

    def on_login(self, iws: IntegrateWebSocket) -> None:
        """
        Callback function called when the WebSocket connection is logged in.

        :param `iws`: The `IntegrateWebSocket` instance.
        :type `iws`: `IntegrateWebSocket`
        :returns: `None`
        """
        pass

    def on_close(
        self, iws: IntegrateWebSocket, code: int, reason: str
    ) -> None:
        """
        Callback function called when the WebSocket connection is closed. To stop reconnection, use `stop` method as shown in the example below.

        .. code-block:: python

            def on_close(iws: IntegrateWebSocket, code: int, reason: str) -> None:
                iws.stop() # this will stop reconnection

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `code`: The close code.
        :param `reason`: The close reason.
        :type `iws`: `IntegrateWebSocket`
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        :note: `RFC6455 <https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1>`_ defines the status codes on connection close.
        """
        pass

    def on_error(
        self, iws: IntegrateWebSocket, code: int, reason: str
    ) -> None:
        """
        Callback function called when the WebSocket connection encounters an error.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `code`: The error code.
        :param `reason`: The error reason.
        :type `iws`: `IntegrateWebSocket`
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        :note: `RFC6455 <https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1>`_ defines the status codes on connection close.
        """
        pass

    def on_reconnection(self, iws: IntegrateWebSocket, retries: int) -> None:
        """
        Callback function called when the WebSocket connection is reconnected.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `retries`: The number of retries.
        :type `iws`: `IntegrateWebSocket`
        :type `retries`: `int`
        :returns: `None`
        """
        pass

    def on_stop_reconnection(self, iws: IntegrateWebSocket) -> None:
        """
        Callback function called when the WebSocket connection stops retrying to reconnect.

        :param `iws`: The `IntegrateWebSocket` instance.
        :type `iws`: `IntegrateWebSocket`
        :returns: `None`
        """
        pass

    def on_exception(self, iws: IntegrateWebSocket, e: Exception) -> None:
        """
        Callback function called when a Python exception occurs.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `e`: The exception.
        :type `iws`: `IntegrateWebSocket`
        :type `e`: `Exception`
        :returns: `None`
        """
        pass

    def on_tick_update(
        self, iws: IntegrateWebSocket, tick: dict[str, str]
    ) -> None:
        """
        Callback function called when the WebSocket connection receives a tick update.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `tick`: The tick update.
        :type `iws`: `IntegrateWebSocket`
        :type `tick`: `dict`
        :returns: `None`
        """
        pass

    def on_order_update(
        self, iws: IntegrateWebSocket, order: dict[str, str]
    ) -> None:
        """
        Callback function called when the WebSocket connection receives an order update.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `order`: The order update.
        :type `iws`: `IntegrateWebSocket`
        :type `order`: `dict`
        :returns: `None`
        """
        pass

    def on_depth_update(
        self, iws: IntegrateWebSocket, depth: dict[str, str]
    ) -> None:
        """
        Callback function called when the WebSocket connection receives a depth update.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `depth`: The depth update.
        :type `iws`: `IntegrateWebSocket`
        :type `depth`: `dict`
        :returns: `None`
        """
        pass

    def on_acknowledgement(
        self, iws: IntegrateWebSocket, ack: dict[str, Any]
    ) -> None:
        """
        Callback function called when the WebSocket connection receives an acknowledgement.

        :param `iws`: The `IntegrateWebSocket` instance.
        :param `ack`: The acknowledgement.
        :type `iws`: `IntegrateWebSocket`
        :type `ack`: `dict`
        :returns: `None`
        """
        pass

    def _on_connect(
        self,
        protocol: IntegrateWebSocketClientProtocol,
        response: ConnectionResponse,
    ) -> None:
        """
        Call `on_connect` callback when connection is established.

        :param `protocol`: The `IntegrateWebSocketClientProtocol` instance.
        :param `response`: The `ConnectionResponse` instance.
        :type `protocol`: `IntegrateWebSocketClientProtocol`
        :type `response`: `ConnectionResponse`
        :returns: `None`
        """
        self._protocol = protocol
        # Reset reconnect on successful reconnect
        self._factory.resetDelay()
        self.on_connect(self, response)

    def _on_open(self) -> None:
        """
        Call `on_open` callback when connection is opened.

        :returns: `None`
        """
        # Relogin and resubscribe if reconnecting
        self.login()
        if self._factory and self._factory.is_reconnection:
            self.resubscribe()
        self._factory.is_reconnection = False
        self.on_open(self)

    def _on_close(self, code: int, reason: str) -> None:
        """
        Call `on_close` callback when connection is closed.

        :param `code`: The close code.
        :param `reason`: The close reason.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        :note: `RFC6455 <https://datatracker.ietf.org/doc/html/rfc6455#section-7.4.1>`_ defines the status codes on connection close
        """
        log.error(
            f"Connection closed: {code} - {reason}"
        ) if self._logging else None
        self.on_close(self, code, reason)

    def _on_error(self, code: int, reason: str) -> None:
        """
        Call `on_error` callback when connection throws an error.

        :param `code`: The error code.
        :param `reason`: The error reason.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        """
        log.error(
            f"Connection error: {code} - {reason}"
        ) if self._logging else None
        self.on_error(self, code, reason)

    def _on_message(
        self,
        payload: bytes,
        is_binary: bool,
    ) -> None:
        """
        Call `on_message` callback when text message is received.

        :param `payload`: The message payload.
        :param `is_binary`: Whether the message is binary.
        :type `payload`: `bytes`
        :type `is_binary`: `bool`
        :returns: `None`
        """
        data: dict[str, Any] = {}
        # Decode payload
        try:
            data = loads(payload.decode('utf-8'))
        except ValueError as e:
            self._on_exception(e)

        # Handle message
        if data["t"] == "ck":
            # Set logged in status
            self.is_logged_in = True if data["s"] == "OK" else False
            if not self.is_logged_in:
                self._on_exception(ValueError("Incorrect login details"))
            self.on_acknowledgement(self, data)
            self.on_login(self)
        elif (
            data["t"] == "tk"
            or data["t"] == "ok"
            or data["t"] == "dk"
            or data["t"] == "uk"
            or data["t"] == "uok"
            or data["t"] == "udk"
        ):
            self.on_acknowledgement(self, data)
        elif data["t"] == "tf":
            self.on_tick_update(self, data)
        elif data["t"] == "om":
            self.on_order_update(self, data)
        elif data["t"] == "df":
            self.on_depth_update(self, data)
        else:
            self._on_exception(KeyError(f"Invalid message: {data}"))

    def _on_reconnection(self, retries: int) -> None:
        """
        Call `on_reconnection` callback when connection is retrying to reconnect.

        :param `retries`: The number of retries.
        :type `retries`: `int`
        :returns: `None`
        """
        self.on_reconnection(self, retries)

    def _on_stop_reconnection(self) -> None:
        """
        Call `on_stop_reconnection` callback when connection stops retrying to reconnect.

        :returns: `None`
        """
        self.on_stop_reconnection(self)

    def _on_exception(self, e: Exception) -> None:
        """
        Call `on_exception` callback when a Python exception occurs.

        :returns: `None`
        """
        self.on_exception(self, e)

    def _close(
        self, code: int | None = None, reason: str | None = None
    ) -> None:
        """
        Close the WebSocket connection.

        :param `code`: The close code.
        :param `reason`: The close reason.
        :type `code`: `int`
        :type `reason`: `str`
        :returns: `None`
        :note: `Close Code Number <https://www.iana.org/assignments/websocket/websocket.xml#close-code-number>`_ defines the status codes on connection close
        """
        self._protocol.sendClose(code, reason) if self._protocol else None  # type: ignore
