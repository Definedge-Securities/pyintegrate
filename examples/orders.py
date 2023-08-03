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

from logging import INFO, basicConfig, info
from typing import Any

from integrate import ConnectToIntegrate, IntegrateOrders

basicConfig(level=INFO)


def main() -> None:
    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(  # nosec: B106
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )

    # Your can access the session keys from a logged in session as below
    # info(conn.get_session_keys())

    # If you have stored the session keys, you can directly set the session keys as below
    # conn.set_session_keys(
    #     "YOUR_UID",
    #     "YOUR_ACTID",
    #     "YOUR_API_SESSION_KEY",
    #     "YOUR_WS_SESSION_KEY",
    # )

    io = IntegrateOrders(conn)

    # Get account balance and cash margin.
    info(io.limits())

    try:
        order: dict[str, Any] = io.place_order(
            exchange=conn.EXCHANGE_TYPE_NSE,
            order_type=conn.ORDER_TYPE_BUY,
            price=0,
            price_type=conn.PRICE_TYPE_MARKET,
            product_type=conn.PRODUCT_TYPE_INTRADAY,
            quantity=1,
            tradingsymbol="SBIN-EQ",
        )
        info(f"Order placed: {order}")

        # Get status of a single order.
        info(io.order(order_id=order["order_id"]))
    except Exception as e:
        info(f"Order placement failed: {e}")

    # Get order book.
    info(io.orders())


if __name__ == "__main__":
    main()
