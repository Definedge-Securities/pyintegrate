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
This example shows how to use the IntegrateWebSocket class to connect to
the Integrate WebSocket API and subscribe to ticks, order updates and
bid-ask depth updates in a daemonized process.
"""

from logging import INFO, basicConfig, info

from integrate import ConnectToIntegrate, IntegrateWebSocket

basicConfig(level=INFO)


def on_login(iws: IntegrateWebSocket) -> None:
    """
    Callback called when the WebSocket connection is established
    and the login is successful.
    """
    # Subscribe to a list of symbols (TCS and TATAMOTORS here).
    tokens: list[tuple[str, str]] = [
        (iws.c2i.EXCHANGE_TYPE_NSE, "11536"),
        (iws.c2i.EXCHANGE_TYPE_NSE, "3456"),
    ]
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_TICK, tokens)
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_ORDER, tokens)
    iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_DEPTH, tokens)


def on_tick_update(iws: IntegrateWebSocket, tick: dict[str, str]) -> None:
    """
    Callback called when a tick update is received.
    """
    info(f"Ticks: {tick}")


def on_order_update(iws: IntegrateWebSocket, order: dict[str, str]) -> None:
    """
    Callback called when an order update is received.
    """
    info(f"Order update : {order}")


def on_depth_update(iws: IntegrateWebSocket, depth: dict[str, str]) -> None:
    """
    Callback called when a bid-ask depth update is received.
    """
    info(f"Depth update : {depth}")


def on_acknowledgement(iws: IntegrateWebSocket, ack: dict[str, str]) -> None:
    """
    Callback called when an acknowledgement is received.
    """
    info(f"Ack : {ack}")


def on_exception(iws: IntegrateWebSocket, e: Exception) -> None:
    """
    Callback to run on Python exceptions.
    """
    info(f"Exception : {e}")
    # Below will close the WebSocket connection.
    # iws.close_on_exception("Closing connection due to exception")


def on_close(iws: IntegrateWebSocket, code: int, reason: str) -> None:
    """
    Callback to run on WebSocket close.
    """
    info(f"Closed : {code} {reason}")
    # Below will stop the event loop and the program will exit.
    # iws.stop()


def main() -> None:
    """
    Main function.
    """
    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(  # nosec: B106
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )
    iws = IntegrateWebSocket(conn)

    # Assign the callbacks to the IntegrateWebSocket object.
    iws.on_login = on_login  # type: ignore
    iws.on_tick_update = on_tick_update  # type: ignore
    iws.on_order_update = on_order_update  # type: ignore
    iws.on_depth_update = on_depth_update  # type: ignore
    iws.on_acknowledgement = on_acknowledgement  # type: ignore
    iws.on_exception = on_exception  # type: ignore
    iws.on_close = on_close  # type: ignore

    # Non-Blocking WebSocket connection below (daemonize=True).
    # If you receive an SSL Error after login, then replace the below line with:
    # iws.connect(daemonize=True, ssl_verify=False)
    iws.connect(daemonize=True)

    # To keep the main thread running, an infinite loop as below should be
    # running. Else, the main thread and thus the daemon thread would exit.
    while True:
        try:
            pass
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
