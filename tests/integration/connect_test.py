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
This module contains integration tests for ConnectToIntegrate class.
"""

from os import remove
from os.path import abspath, dirname, isfile, join

from pytest import raises

from integrate import ConnectToIntegrate


def test_successful_login(c2i: ConnectToIntegrate) -> None:
    """
    Test successful login.

    :return: None
    """
    # Assert that the response contains the required keys
    assert c2i.actid != ""
    assert c2i.uid != ""
    assert c2i.api_session_key != ""
    assert c2i.ws_session_key != ""


def test_unsuccessful_login() -> None:
    """
    Test unsuccessful login.

    :return: None
    """
    with raises(Exception) as e:
        # Login to Definedge Securities Integrate
        c2i = ConnectToIntegrate()
        c2i.login(  # nosec: B106
            api_token="",
            api_secret="",
        )
        # Assert that the response is of an invalid login
        assert e.value == "Invalid api_token or api_secret"


def test_storing_session_keys(c2i: ConnectToIntegrate) -> None:
    """
    Test storing session keys of ConnectToIntegrate class.

    :param c2i: Instance of ConnectToIntegrate class
    :type c2i: ConnectToIntegrate
    :return: None
    """
    c2i.set_session_keys(
        "integration_test",
        "integration_test",
        "integration_test",
        "integration_test",
    )
    assert c2i.uid == "integration_test"
    assert c2i.actid == "integration_test"
    assert c2i.api_session_key == "integration_test"
    assert c2i.ws_session_key == "integration_test"


def test_getting_session_keys(c2i: ConnectToIntegrate) -> None:
    """
    Test getting session keys from ConnectToIntegrate class.

    :param c2i: Instance of ConnectToIntegrate class
    :type c2i: ConnectToIntegrate
    :return: None
    """
    c2i.set_session_keys(
        "integration_test",
        "integration_test",
        "integration_test",
        "integration_test",
    )
    assert c2i.get_session_keys() == (
        "integration_test",
        "integration_test",
        "integration_test",
        "integration_test",
    )


def test_symbols(c2i: ConnectToIntegrate) -> None:
    """
    Test symbols generator.

    :param c2i: Instance of ConnectToIntegrate class
    :type c2i: ConnectToIntegrate
    :return: None
    """
    symbol_filename: str = abspath(
        join(dirname(__file__), "..", "..", "allmaster.csv")
    )
    # Remove the file if it exists
    if isfile(symbol_filename):
        remove(symbol_filename)

    # Generate symbols and assert that the keys are present
    assert "token" in next(c2i.symbols)
    assert "symbol" in next(c2i.symbols)
