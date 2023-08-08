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
This module contains unit tests for ConnectToIntegrate class.
"""

from hashlib import sha256
from os import remove
from os.path import abspath, dirname, isfile, join
from urllib.parse import urljoin

from pytest import raises
from responses import GET, POST, activate, add
from responses.matchers import header_matcher, json_params_matcher

from integrate import ConnectToIntegrate
from tests.responses_helper import get_mock_response


@activate
def test_successful_login() -> None:
    """
    Test successful login.

    :return: None
    """
    test_login_url: str = "http://signin-defsec-unit-test"
    test_base_url: str = "http://integrate-defsec-unit-test/"
    api_token: str = "unit_test"
    api_secret: str = "unit_test"
    otp_token: str = "unit_test"
    otp: str = "123456"
    ac: str = sha256(
        f"{otp_token}{otp}{api_secret}".encode("utf-8")
    ).hexdigest()
    # Add a mock response for the login endpoint
    add(
        method=GET,
        url=urljoin(
            test_login_url,
            f"login/{api_token}",
        ),
        match=[
            header_matcher(
                {
                    "api_secret": api_secret,
                }
            )
        ],
        body=get_mock_response("login_step_1.json"),
        content_type="application/json",
    )
    # Add a mock response for the OTP endpoint
    add(
        method=POST,
        url=urljoin(
            test_login_url,
            "token",
        ),
        match=[
            json_params_matcher(
                {
                    "otp_token": otp_token,
                    "otp": otp,
                    "ac": ac,
                }
            )
        ],
        body=get_mock_response("login_step_2.json"),
        content_type="application/json",
    )
    # Add a passthrough response for the symbols' master file endpoint
    add(
        method=GET,
        url="https://app.definedgesecurities.com/public/allmaster.zip",
        body="{}",
        passthrough=True,
    )
    # Login to Definedge Securities Integrate
    c2i = ConnectToIntegrate(
        login_url=test_login_url,
        base_url=test_base_url,
    )
    c2i.login(
        api_token=api_token,
        api_secret=api_secret,
        totp=otp,
    )
    # Assert that the response is a dict and contains the required keys
    assert c2i.actid == "unit_test"
    assert c2i.uid == "unit_test"
    assert c2i.api_session_key == "unit_test"
    assert c2i.ws_session_key == "unit_test"


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
            totp="",
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
        uid="unit_test",
        actid="unit_test",
        api_session_key="unit_test",
        ws_session_key="unit_test",
    )
    assert c2i.uid == "unit_test"
    assert c2i.actid == "unit_test"
    assert c2i.api_session_key == "unit_test"
    assert c2i.ws_session_key == "unit_test"
    assert c2i.login_url == "http://signin-defsec-unit-test"
    assert c2i.base_url == "http://integrate-defsec-unit-test/"


def test_getting_session_keys(c2i: ConnectToIntegrate) -> None:
    """
    Test getting session keys from ConnectToIntegrate class.

    :param c2i: Instance of ConnectToIntegrate class
    :type c2i: ConnectToIntegrate
    :return: None
    """
    c2i.set_session_keys(
        uid="unit_test",
        actid="unit_test",
        api_session_key="unit_test",
        ws_session_key="unit_test",
    )
    assert c2i.get_session_keys() == (
        "unit_test",
        "unit_test",
        "unit_test",
        "unit_test",
    )


@activate
def test_symbols(c2i: ConnectToIntegrate) -> None:
    """
    Test symbols generator.

    :param c2i: Instance of ConnectToIntegrate class
    :type c2i: ConnectToIntegrate
    :return: None
    """
    # Add a passthrough response for the symbols' master file endpoint
    add(
        method=GET,
        url="https://app.definedgesecurities.com/public/allmaster.zip",
        body="{}",
        passthrough=True,
    )
    symbol_filename: str = abspath(
        join(dirname(__file__), "..", "..", "allmaster.csv")
    )
    # Remove the file if it exists
    if isfile(symbol_filename):
        remove(symbol_filename)

    # Generate symbols and assert that the keys are present
    assert "token" in next(c2i.symbols)
    assert "symbol" in next(c2i.symbols)


def test_logging(c2i_with_logging: ConnectToIntegrate) -> None:
    """
    Test logging.

    :param c2i_with_logging: Instance of ConnectToIntegrate class with logging enabled
    :type c2i_with_logging: ConnectToIntegrate
    :return: None
    """
    # Assert that the base_url is set correctly
    assert c2i_with_logging.base_url == "http://integrate-defsec-unit-test/"
