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
This module contains integration tests for IntegrateData class.
"""

from datetime import datetime
from typing import Any

from integrate import ConnectToIntegrate, IntegrateData
from tests.responses_helper import compare_keys


def test_fetching_historical_data(
    c2i: ConnectToIntegrate, ic: IntegrateData
) -> None:
    """
    Test fetching historical data for a symbol.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    # Fetch historical data
    history: dict[str, Any] = next(
        ic.historical_data(
            exchange=c2i.EXCHANGE_TYPE_NSE,
            trading_symbol="ACC-EQ",
            timeframe=c2i.TIMEFRAME_TYPE_MIN,
            start=datetime(2023, 6, 30, 0, 0),
            end=datetime(2023, 7, 3, 15, 30),
        )
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(history, dict)
    assert "datetime" in history
    assert "open" in history
    assert "high" in history
    assert "low" in history
    assert "close" in history
    assert "volume" in history


def test_fetching_quote(c2i: ConnectToIntegrate, ic: IntegrateData) -> None:
    """
    Test fetching quote for a symbol.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    # Fetch quote
    quote: dict[str, Any] = ic.quotes(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol="ACC-EQ",
    )

    # Assert that the response is a dict and contains the required keys
    assert isinstance(quote, dict)
    assert compare_keys("quotes.json", quote)


def test_fetching_security_info(
    c2i: ConnectToIntegrate, ic: IntegrateData
) -> None:
    """
    Test fetching security info.

    :param c2i: ConnectToIntegrate object
    :param ic: IntegrateData object
    :return: None
    """
    # Fetch security info
    sec_info: dict[str, Any] = ic.security_information(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        trading_symbol="ACC-EQ",
    )

    # Assert that the response is a dict and contains the required keys
    assert isinstance(sec_info, dict)
    assert compare_keys("security_information.json", sec_info)
