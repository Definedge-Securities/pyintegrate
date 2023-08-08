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
the Integrate Orders API and place a market order, get an order's status
using order_id and get the order book. This example also shows how to
login to Integrate and save the session keys in a .env file, so that
you don't have to login again and again.
"""

from logging import INFO, basicConfig, info
from os import environ
from typing import Any

from dotenv import (  # pip install python-dotenv
    find_dotenv,
    load_dotenv,
    set_key,
)

from integrate import ConnectToIntegrate, IntegrateOrders

basicConfig(level=INFO)
dotenv_file: str = find_dotenv()
load_dotenv(dotenv_file)


def main() -> None:
    """
    Main function
    """
    try:
        # Get the API token and secret from environment variables.
        api_token: str = environ["INTEGRATE_API_TOKEN"]
        api_secret: str = environ["INTEGRATE_API_SECRET"]
    except KeyError:
        raise KeyError(
            "Please set INTEGRATE_API_TOKEN and INTEGRATE_API_SECRET in .env file."
        )

    # Initialise the connection.
    conn = ConnectToIntegrate()
    # Login to Integrate.
    try:
        uid: str = environ["INTEGRATE_UID"]
        actid: str = environ["INTEGRATE_ACTID"]
        api_session_key: str = environ["INTEGRATE_API_SESSION_KEY"]
        ws_session_key: str = environ["INTEGRATE_WS_SESSION_KEY"]
        conn.set_session_keys(uid, actid, api_session_key, ws_session_key)
        # Please note that the session keys are valid for 24 hours. After that you
        # will have to login again. The logic to handle this is left to the user.
    except KeyError:
        conn.login(
            api_token=api_token,
            api_secret=api_secret,
        )
        (uid, actid, api_session_key, ws_session_key) = conn.get_session_keys()
        environ["INTEGRATE_UID"] = uid
        environ["INTEGRATE_ACTID"] = actid
        environ["INTEGRATE_API_SESSION_KEY"] = api_session_key
        environ["INTEGRATE_WS_SESSION_KEY"] = ws_session_key
        set_key(dotenv_file, "INTEGRATE_UID", uid)
        set_key(dotenv_file, "INTEGRATE_ACTID", actid)
        set_key(dotenv_file, "INTEGRATE_API_SESSION_KEY", api_session_key)
        set_key(dotenv_file, "INTEGRATE_WS_SESSION_KEY", ws_session_key)
        info("Login successful.")

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
