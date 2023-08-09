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
bid-ask depth updates. The websocket connection is blocking, so you have
to use the callbacks to manage the connection.
"""

from logging import INFO, basicConfig, info
from typing import Union

from integrate import ConnectToIntegrate, IntegrateWebSocket

basicConfig(level=INFO)

# Initialise the connection and login.
conn = ConnectToIntegrate()
conn.login(  # nosec: B106
    api_token="YOUR_API_TOKEN",
    api_secret="YOUR_API_SECRET",
)

# List of symbols (TCS and TATAMOTORS here) to subscribe to.
symbols: list[tuple[str, str]] = [
    (conn.EXCHANGE_TYPE_NSE, "TCS-EQ"),
    (conn.EXCHANGE_TYPE_NSE, "TATAMOTORS-EQ"),
]
# Tokens of the above symbols.
tokens: list[tuple[str, str]] = []


def get_token_for_symbol(exchange: str, symbol: str) -> tuple[str, str]:
    """
    Get the token for a symbol from the symbols file.
    """
    if exchange not in conn.exchange_types:
        raise ValueError("Invalid exchange type")

    token: Union[str, None] = next(
        (
            i["token"]
            for i in conn.symbols
            if i["segment"] == exchange and i["trading_symbol"] == symbol
        ),
        None,
    )
    if token:
        return (exchange, token)
    else:
        raise Exception(f"Token not found for {symbol} in symbols file")


def on_login(iws: IntegrateWebSocket) -> None:
    """
    Callback called when the WebSocket connection is established and the login is successful.
    """
    for exchange, symbol in symbols:
        tokens.append(get_token_for_symbol(exchange, symbol))
    # Subscribe to a list of symbols. You can have different lists for different subscriptions.
    iws.subscribe(conn.SUBSCRIPTION_TYPE_TICK, tokens)
    iws.subscribe(conn.SUBSCRIPTION_TYPE_DEPTH, tokens)


def on_tick_update(iws: IntegrateWebSocket, tick: dict[str, str]) -> None:
    """
    Callback to receive tick updates.
    """
    info(f"Ticks: {tick}")


def on_order_update(iws: IntegrateWebSocket, order: dict[str, str]) -> None:
    """
    Callback called when an order update is received.
    """
    info(f"Order update : {order}")


def on_depth_update(iws: IntegrateWebSocket, depth: dict[str, str]) -> None:
    """
    Callback to receive bid-ask depth updates.
    """
    info(f"Depth update : {depth}")


def on_exception(iws: IntegrateWebSocket, e: Exception) -> None:
    """
    Callback to run on Python exceptions.
    """
    info(f"Exception : {e}")


def on_close(iws: IntegrateWebSocket, code: int, reason: str) -> None:
    """
    Callback to run on WebSocket close.
    """
    info(f"Closed : {code} {reason}")
    # iws.stop()  # This will stop the event loop and the program will exit.


def main() -> None:
    """
    Main function
    """
    iws = IntegrateWebSocket(conn)

    # Assign the callbacks.
    iws.on_login = on_login  # type: ignore
    iws.on_tick_update = on_tick_update  # type: ignore
    iws.on_order_update = on_order_update  # type: ignore
    iws.on_depth_update = on_depth_update  # type: ignore
    iws.on_exception = on_exception  # type: ignore
    iws.on_close = on_close  # type: ignore

    # Blocking WebSocket connection below. Nothing after this will run.
    # You have to use the callbacks for further management.
    iws.connect()


if __name__ == "__main__":
    main()
