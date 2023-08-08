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
the Integrate Orders API and get the margin requirements for a basket
of securities.
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

    # Get margin requirements for a basket of securities.
    orders: list[dict[str, Any]] = [
        {
            "exchange": io.c2i.EXCHANGE_TYPE_NSE,
            "tradingsymbol": "SBIN-EQ",
            "quantity": 50,
            "price": 0,
            "product_type": io.c2i.PRODUCT_TYPE_INTRADAY,
            "order_type": io.c2i.ORDER_TYPE_BUY,
            "price_type": io.c2i.PRICE_TYPE_MARKET,
        },
        {
            "exchange": io.c2i.EXCHANGE_TYPE_NSE,
            "tradingsymbol": "TCS-EQ",
            "quantity": 10,
            "price": 0,
            "product_type": io.c2i.PRODUCT_TYPE_CNC,
            "order_type": io.c2i.ORDER_TYPE_BUY,
            "price_type": io.c2i.PRICE_TYPE_MARKET,
        },
    ]

    info(io.margins(orders=orders))


if __name__ == "__main__":
    main()
