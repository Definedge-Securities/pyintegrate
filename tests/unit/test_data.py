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

from datetime import datetime
from typing import Any, Union
from urllib.parse import urljoin

from responses import GET, activate, add

from integrate import ConnectToIntegrate, IntegrateData
from tests.responses_helper import get_mock_response


@activate
def test_fetching_historical_data(
    c2i: ConnectToIntegrate, ic: IntegrateData
) -> None:
    """
    Test fetching historical data for a symbol.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    exchange: str = c2i.EXCHANGE_TYPE_NSE
    timeframe: str = c2i.TIMEFRAME_TYPE_DAY
    trading_symbol: str = "ACC-EQ"
    start: datetime = datetime.strptime("300620230915", "%d%m%Y%H%M")
    end: datetime = datetime.strptime("300620231530", "%d%m%Y%H%M")
    token: Union[str, None] = next(
        (
            i["token"]
            for i in c2i.symbols
            if i["segment"] == c2i.EXCHANGE_TYPE_NSE
            and i["trading_symbol"] == trading_symbol
        ),
        None,
    )
    # Add a mock response for the historical data endpoint
    add(
        method=GET,
        url=urljoin(
            "https://data.definedgesecurities.com/sds/history/",
            f"{exchange}/{token}/{timeframe}/{start.strftime('%d%m%Y%H%M')}/{end.strftime('%d%m%Y%H%M')}",
        ),
        body=get_mock_response("historical.csv"),
        content_type="text/csv",
    )
    # Fetch historical data
    data: dict[str, Any] = next(
        ic.historical_data(
            exchange=c2i.EXCHANGE_TYPE_NSE,
            trading_symbol=trading_symbol,
            timeframe=timeframe,
            start=start,
            end=end,
        )
    )
    # Assert that the response contains the required keys
    assert isinstance(data, dict)
    assert "datetime" in data
    assert "open" in data
    assert "high" in data
    assert "low" in data
    assert "close" in data
    assert "volume" in data


@activate
def test_fetching_quotes(c2i: ConnectToIntegrate, ic: IntegrateData) -> None:
    """
    Test fetching quotes for a symbol.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    trading_symbol: str = "ACC-EQ"
    token: Union[str, None] = next(
        (
            i["token"]
            for i in c2i.symbols
            if i["segment"] == c2i.EXCHANGE_TYPE_NSE
            and i["trading_symbol"] == trading_symbol
        ),
        None,
    )
    # Add a mock response for the quote endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"quotes/{c2i.EXCHANGE_TYPE_NSE}/{token}",
        ),
        body=get_mock_response("quotes.json"),
        content_type="application/json",
    )
    # Fetch quote
    quote: dict[str, Any] = ic.quotes(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol=trading_symbol,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(quote, dict)
    assert "status" in quote
    assert "ltp" in quote
    assert "volume" in quote
    assert "best_bid_price1" in quote
    assert "best_ask_price1" in quote
    assert "best_bid_qty1" in quote
    assert "best_ask_qty1" in quote


@activate
def test_fetching_security_info(
    c2i: ConnectToIntegrate, ic: IntegrateData
) -> None:
    """
    Test fetching security info.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    trading_symbol: str = "ACC-EQ"
    token: Union[str, None] = next(
        (
            i["token"]
            for i in c2i.symbols
            if i["segment"] == c2i.EXCHANGE_TYPE_NSE
            and i["trading_symbol"] == trading_symbol
        ),
        None,
    )
    # Add a mock response for the security info endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"securityinfo/{c2i.EXCHANGE_TYPE_NSE}/{token}",
        ),
        body=get_mock_response("security_information.json"),
        content_type="application/json",
    )
    # Fetch security info
    sec_info: dict[str, Any] = ic.security_information(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol=trading_symbol,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(sec_info, dict)
    assert "status" in sec_info
    assert "company_name" in sec_info
    assert "isin" in sec_info
