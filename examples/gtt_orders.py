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
This example shows how to use the IntegrateOrders class to connect to
the Integrate Orders API and place a GTT order and get the GTT order book.
"""

from logging import INFO, basicConfig, info
from typing import Any

from integrate import ConnectToIntegrate, IntegrateOrders

basicConfig(level=INFO)


def main() -> None:
    """
    Main function
    """
    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(  # nosec: B106
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )
    io = IntegrateOrders(conn)

    try:
        order: dict[str, Any] = io.place_gtt_order(
            exchange=conn.EXCHANGE_TYPE_NSE,
            order_type=conn.ORDER_TYPE_BUY,
            price=620,
            quantity=1,
            tradingsymbol="SBIN-EQ",
            alert_price=619.95,
            condition=conn.GTT_CONDITION_LTP_ABOVE,
        )
        info(f"GTT Order placed: {order}")
    except Exception as e:
        info(f"GTT Order placement failed: {e}")

    # Get GTT order book.
    info(io.gtt_orders())


if __name__ == "__main__":
    main()
