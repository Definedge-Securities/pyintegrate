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
This module contains the IntegrateData class which is used to connect to
the Integrate Data API and fetch historical data, quotes and security
information.

Example:

.. code-block:: python

    from datetime import datetime

    from integrate import ConnectToIntegrate, IntegrateData

    c2i = ConnectToIntegrate()
    c2i.login(api_token="YOUR_API_TOKEN", api_secret="YOUR_API_SECRET")

    ic = IntegrateData(connect_to_integrate=c2i)

    # Fetch historical data for a symbol
    historical_data = ic.historical_data(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol="ACC-EQ",
        timeframe=c2i.TIMEFRAME_TYPE_DAY,
        start=datetime.strptime("300620230915", "%d%m%Y%H%M"),
        end=datetime.strptime("300620231530", "%d%m%Y%H%M"),
    )

    # Fetch quotes for a symbol
    quotes = ic.quotes(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol="ACC-EQ",
    )

    # Fetch security information for a symbol
    security_information = ic.security_information(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol="ACC-EQ",
    )
"""

from datetime import datetime
from logging import DEBUG, Logger, getLogger
from typing import Any, Generator, Union

from integrate import ConnectToIntegrate

logger: Logger = getLogger(__name__)
logger.setLevel(DEBUG)


class IntegrateData:
    """
    Definedge Securities Integrate Data API class

    :param `connect_to_integrate`: The connection object.
    :param `logging`: Enable or disable logging. Defaults to `False`. If set to True, will print all requests and responses to logger.
    :type `connect_to_integrate`: `ConnectToIntegrate`
    :type `logging`: `bool`
    """

    def __init__(
        self,
        connect_to_integrate: ConnectToIntegrate,
        logging: bool = False,
    ) -> None:
        self._logging: bool = logging

        self.c2i: ConnectToIntegrate = connect_to_integrate

    def historical_data(
        self,
        exchange: str,
        trading_symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
    ) -> Generator[dict[str, Any], None, None]:
        """
        Retrieve historical data for an security.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `trading_symbol`: Trading symbol of the security.
        :param `timeframe`: Timeframe of the data. day or minute are supported.
        :param `start`: Start date of the data.
        :param `end`: End date of the data.
        :type `exchange`: `str`
        :type `trading_symbol`: `str`
        :type `timeframe`: `str`
        :type `start`: `datetime`
        :type `end`: `datetime`
        :returns: Historical data for the security.
        :rtype: `Generator[dict[str, Any], None, None]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if timeframe not in self.c2i.timeframe_types:
            raise ValueError("Invalid timeframe")

        token: Union[str, None] = next(
            (
                i["token"]
                for i in self.c2i.symbols
                if i["segment"] == exchange
                and i["trading_symbol"] == trading_symbol
            ),
            None,
        )
        if token:
            try:
                historical_data: dict[str, Any] = self.c2i.send_request(
                    route_prefix="https://data.definedgesecurities.com/sds/history/",
                    route=f"{exchange}/{token}/{timeframe}/{start.strftime('%d%m%Y%H%M')}/{end.strftime('%d%m%Y%H%M')}",
                    method="GET",
                )
                for line in historical_data["data"]:
                    if len(line):
                        data: list[str] = line.split(",")
                        if len(data) == 7:
                            yield {
                                "datetime": datetime.strptime(
                                    data[0], "%d%m%Y%H%M"
                                ),
                                "open": float(data[1]),
                                "high": float(data[2]),
                                "low": float(data[3]),
                                "close": float(data[4]),
                                "volume": int(data[5]),
                                "oi": int(data[6]),
                            }
                        else:
                            yield {
                                "datetime": datetime.strptime(
                                    data[0], "%d%m%Y%H%M"
                                ),
                                "open": float(data[1]),
                                "high": float(data[2]),
                                "low": float(data[3]),
                                "close": float(data[4]),
                                "volume": int(data[5]),
                            }
            except Exception as e:
                raise e
        else:
            raise Exception(
                f"Token not found for {trading_symbol} in symbols file"
            )

    def quotes(self, exchange: str, trading_symbol: str) -> dict[str, Any]:
        """
        Retrieve quotes for an security.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `trading_symbol`: Trading symbol of the security.
        :type `exchange`: `str`
        :type `trading_symbol`: `str`
        :returns: Quote for the security.
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        token: Union[str, None] = next(
            (
                i["token"]
                for i in self.c2i.symbols
                if i["segment"] == exchange
                and i["trading_symbol"] == trading_symbol
            ),
            None,
        )
        if token:
            return self.c2i.send_request(
                route_prefix=self.c2i.base_url,
                route=f"quotes/{exchange}/{token}",
                method="GET",
            )
        else:
            raise Exception(
                f"Token not found for {trading_symbol} in symbols file"
            )

    def security_information(
        self, exchange: str, trading_symbol: str
    ) -> dict[str, Any]:
        """
        Retrieve details about an security.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `trading_symbol`: Trading symbol of the security.
        :type `exchange`: `str`
        :type `trading_symbol`: `str`
        :returns: Details about the security.
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        token: Union[str, None] = next(
            (
                i["token"]
                for i in self.c2i.symbols
                if i["segment"] == exchange
                and i["trading_symbol"] == trading_symbol
            ),
            None,
        )
        if token:
            return self.c2i.send_request(
                route_prefix=self.c2i.base_url,
                route=f"securityinfo/{exchange}/{token}",
                method="GET",
            )
        else:
            raise Exception(
                f"Token not found for {trading_symbol} in symbols file"
            )
