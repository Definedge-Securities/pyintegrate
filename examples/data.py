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
This example shows how to use the IntegrateData class to connect to
the Integrate Data API and fetch quotes, security information and
historical data for a symbol.
"""

from datetime import datetime, timedelta
from logging import INFO, basicConfig, info
from typing import Any, Generator

from integrate import ConnectToIntegrate, IntegrateData

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

    ic = IntegrateData(conn)

    # Get quote for NSE:SBIN-EQ
    info(ic.quotes(exchange=conn.EXCHANGE_TYPE_NSE, trading_symbol="SBIN-EQ"))

    # Get security information for NSE:SBIN-EQ
    info(
        ic.security_information(
            exchange=conn.EXCHANGE_TYPE_NSE, trading_symbol="SBIN-EQ"
        )
    )

    today: datetime = datetime.today()
    yesterday: datetime = today - timedelta(days=1)

    # Get historical data for NSE:SBIN-EQ
    history: Generator[dict[str, Any], None, None] = ic.historical_data(
        exchange=conn.EXCHANGE_TYPE_NSE,
        trading_symbol="SBIN-EQ",
        timeframe=conn.TIMEFRAME_TYPE_MIN,
        start=yesterday,
        end=today,
    )

    for data in history:
        info(data)


if __name__ == "__main__":
    main()
