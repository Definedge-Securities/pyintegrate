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
This module contains the ConnectToIntegrate class which is used to connect to
the Integrate API and login, get symbols and send requests.

Example:

.. code-block:: python

    from integrate import ConnectToIntegrate

    # Create a ConnectToIntegrate object
    c2i = ConnectToIntegrate()

    # Login to Integrate
    c2i.login(api_token="YOUR_API_TOKEN", api_secret="YOUR_API_SECRET")

    # Get symbols
    for symbol in c2i.symbols:
        print(symbol)
"""

from csv import reader
from hashlib import sha256
from io import BytesIO
from logging import DEBUG, Logger, getLogger
from os import remove
from os.path import abspath, dirname, join
from typing import Any, Callable, Generator, Union
from urllib.parse import urljoin
from zipfile import ZipFile

from requests import Response, Session

logger: Logger = getLogger(__name__)
logger.setLevel(DEBUG)


class ConnectToIntegrate:
    """
    Definedge Securities Integrate Connection API class

    :param `login_url`: URL to use for login
    :param `base_url`: Base URL to use for API requests
    :param `timeout`: Maximum time (seconds) for which the API client will wait for a request to complete before it fails. Defaults to 10 seconds.
    :param `logging`: Enable or disable logging. Defaults to `False`. If set to True, will print all requests and responses to logger.
    :param `proxies`: To set requests proxy. Required when the client's requests are going through a proxy server. Check `requests documentation <http://docs.python-requests.org/en/master/user/advanced/#proxies>`_ for usage and examples.
    :type `login_url`: `str | None`
    :type `base_url`: `str | None`
    :type `timeout`: `int | None`
    :type `logging`: `bool`
    :type `proxies`: `dict[str, str] | None`
    """

    EXCHANGE_TYPE_NSE = "NSE"
    EXCHANGE_TYPE_BSE = "BSE"
    EXCHANGE_TYPE_NFO = "NFO"
    EXCHANGE_TYPE_CDS = "CDS"
    EXCHANGE_TYPE_MCX = "MCX"

    ORDER_TYPE_BUY = "BUY"
    ORDER_TYPE_SELL = "SELL"

    PRICE_TYPE_MARKET = "MARKET"
    PRICE_TYPE_LIMIT = "LIMIT"
    PRICE_TYPE_SL_MKT = "SL-MARKET"
    PRICE_TYPE_SL_LMT = "SL-LIMIT"

    PRODUCT_TYPE_CNC = "CNC"
    PRODUCT_TYPE_INTRADAY = "INTRADAY"
    PRODUCT_TYPE_NORMAL = "NORMAL"

    SUBSCRIPTION_TYPE_TICK = "TICK"
    SUBSCRIPTION_TYPE_ORDER = "ORDER"
    SUBSCRIPTION_TYPE_DEPTH = "DEPTH"

    VALIDITY_TYPE_DAY = "DAY"
    VALIDITY_TYPE_IOC = "IOC"
    VALIDITY_TYPE_EOS = "EOS"

    ORDER_STATUS_NEW = "NEW"
    ORDER_STATUS_OPEN = "OPEN"
    ORDER_STATUS_COMPLETE = "COMPLETE"
    ORDER_STATUS_CANCELLED = "CANCELED"
    ORDER_STATUS_REJECTED = "REJECTED"
    ORDER_STATUS_REPLACED = "REPLACED"

    GTT_CONDITION_LTP_BELOW = "LTP_BELOW"
    GTT_CONDITION_LTP_ABOVE = "LTP_ABOVE"

    TIMEFRAME_TYPE_MIN = "minute"
    TIMEFRAME_TYPE_DAY = "day"

    def __init__(
        self,
        login_url: Union[str, None] = None,
        base_url: Union[str, None] = None,
        timeout: Union[int, None] = None,
        logging: bool = False,
        proxies: Union[dict[str, str], None] = None,
    ) -> None:
        # Set default values for the connection.
        self._logging: bool = logging
        self._timeout: int = timeout or 10  # in seconds
        self._proxies: dict[str, str] = proxies if proxies else {}

        # Start a requests session.
        self._req_sess: Session = Session()

        # Initialize the session variables.
        self.uid: str = ""
        self.actid: str = ""
        self.api_session_key: str = ""
        self.ws_session_key: str = ""

        # Set to default values if not provided.
        self.login_url: str = (
            login_url
            if login_url
            else "https://signin.definedgesecurities.com/auth/realms/debroking/dsbpkc/"
        )
        self.base_url: str = (
            base_url
            if base_url
            else "https://integrate.definedgesecurities.com/dart/v1/"
        )

        self.session_expired_callback: Union[Callable[[], None], None] = None

        # Initialize the exchange, order, price, product and subscription types.
        self.exchange_types: list[str] = [
            self.EXCHANGE_TYPE_NSE,
            self.EXCHANGE_TYPE_BSE,
            self.EXCHANGE_TYPE_NFO,
            self.EXCHANGE_TYPE_CDS,
            self.EXCHANGE_TYPE_MCX,
        ]
        self.order_types: list[str] = [
            self.ORDER_TYPE_BUY,
            self.ORDER_TYPE_SELL,
        ]
        self.price_types: list[str] = [
            self.PRICE_TYPE_MARKET,
            self.PRICE_TYPE_LIMIT,
            self.PRICE_TYPE_SL_MKT,
            self.PRICE_TYPE_SL_LMT,
        ]
        self.product_types: list[str] = [
            self.PRODUCT_TYPE_CNC,
            self.PRODUCT_TYPE_INTRADAY,
            self.PRODUCT_TYPE_NORMAL,
        ]
        self.subscription_types: list[str] = [
            self.SUBSCRIPTION_TYPE_TICK,
            self.SUBSCRIPTION_TYPE_ORDER,
            self.SUBSCRIPTION_TYPE_DEPTH,
        ]
        self.gtt_condition_types: list[str] = [
            self.GTT_CONDITION_LTP_BELOW,
            self.GTT_CONDITION_LTP_ABOVE,
        ]
        self.timeframe_types: list[str] = [
            self.TIMEFRAME_TYPE_MIN,
            self.TIMEFRAME_TYPE_DAY,
        ]

    def login(
        self,
        api_token: str,
        api_secret: str,
        totp: Union[str, None] = None,
    ) -> None:
        """
        Login to Definedge Securities Integrate

        :param `api_token`: Your Definedge Securities API Token. Available at https://myaccount.definedgesecurities.com/mydetails -> Show My API Secret
        :param `api_secret`: Your Definedge Securities API Secret. Available at https://myaccount.definedgesecurities.com/mydetails -> Show My API Secret
        :param `totp`: Your 6-digit External TOTP for two-factor authentication. Enable at https://myaccount.definedgesecurities.com/security
        :type `api_token`: `str`
        :type `api_secret`: `str`
        :type `totp`: `str | None`
        """
        if api_token and api_secret:
            try:
                # Get OTP token
                r: dict[str, Any] = self.send_request(
                    route_prefix=self.login_url,
                    route=f"login/{api_token}",
                    method="GET",
                    extra_headers={"api_secret": api_secret},
                )
                otp_token: str = r["otp_token"]
                try:
                    # Get OTP/TOTP for 2FA
                    otp: str = (
                        input("Enter OTP/External TOTP: ")
                        if not totp
                        else totp
                    )
                except KeyboardInterrupt:
                    raise ValueError("No OTP/TOTP provided")
                ac: str = sha256(
                    f"{otp_token}{otp}{api_secret}".encode("utf-8")
                ).hexdigest()
                # Get session keys
                r = self.send_request(
                    route_prefix=self.login_url,
                    route="token",
                    method="POST",
                    json_params={
                        "otp_token": otp_token,
                        "otp": otp,
                        "ac": ac,
                    },
                )
                self.set_session_keys(
                    r["uid"], r["actid"], r["api_session_key"], r["susertoken"]
                )
                try:
                    # Get symbols
                    symbols_filename: str = abspath(
                        join(dirname(__file__), "allmaster.csv")
                    )
                    remove(symbols_filename)
                except FileNotFoundError:
                    pass
                next(self.symbols)
            except Exception as e:
                raise Exception(e)
        else:
            raise ValueError("Invalid api_token or api_secret")

    def get_session_keys(
        self,
    ) -> tuple[str, str, str, str]:
        """
        Get stored session keys

        :return: The session keys
        :rtype: `tuple[str, str, str, str]`
        """
        return (
            self.uid,
            self.actid,
            self.api_session_key,
            self.ws_session_key,
        )

    def set_session_keys(
        self,
        uid: str,
        actid: str,
        api_session_key: str,
        ws_session_key: str,
    ) -> None:
        """
        Store session keys

        :param `uid`: Your Definedge Securities login UCC id
        :param `actid`: Your Definedge Securities login account id
        :param `api_session_key`: Your Definedge Securities API session key
        :param `ws_session_key`: Your Definedge Securities WebSocket session key
        :type `uid`: `str`
        :type `actid`: `str`
        :type `api_session_key`: `str`
        :type `ws_session_key`: `str`
        """
        self.uid = uid
        self.actid = actid
        self.api_session_key = api_session_key
        self.ws_session_key = ws_session_key

    @property
    def symbols(self) -> Generator[dict[str, str], None, None]:
        """
        Download the master file for symbols and create a generator

        :return: A generator of symbols
        :rtype: `Generator[dict[str, str], None, None]`
        """
        # Download the master file if not present
        symbols_filename: str = abspath(
            join(dirname(__file__), "allmaster.csv")
        )
        try:
            open(symbols_filename, "r")
        except FileNotFoundError:
            r: Response = self._req_sess.request(
                method="GET",
                url="https://app.definedgesecurities.com/public/allmaster.zip",
                verify=True,
                allow_redirects=True,
                timeout=self._timeout,
                proxies=self._proxies,
            )
            with ZipFile(BytesIO(r.content), "r") as z:
                z.extract("allmaster.csv", abspath(dirname(__file__)))

        # Create a generator of symbols
        with open(symbols_filename, "r") as fp:
            for line in reader(fp):
                yield {
                    "segment": line[0],
                    "token": line[1],
                    "symbol": line[2],
                    "trading_symbol": line[3],
                    "instrument_type": line[4],
                    "expiry": line[5],
                    "tick_size": line[6],
                    "lot_size": line[7],
                    "option_type": line[8],
                    "strike": str(
                        int(
                            int(line[9]) / (int(line[11]) * 10 ^ int(line[10]))
                        )
                    ),
                    "isin": line[12],
                    "price_mult": line[13],
                }

    def send_request(  # noqa: C901
        self,
        route_prefix: str,
        route: str,
        method: str,
        url_params: Union[dict[str, str], None] = None,
        json_params: Union[dict[str, Any], None] = None,
        data_params: Union[dict[str, Any], None] = None,
        query_params: Union[dict[str, str], None] = None,
        extra_headers: Union[dict[str, str], None] = None,
    ) -> dict[str, Any]:
        """
        Make an HTTP request.

        :param `route_prefix`: The prefix of the route
        :param `route`: The route
        :param `method`: The HTTP method
        :param `url_params`: The URL parameters
        :param `json_params`: The JSON parameters
        :param `data_params`: The data parameters
        :param `query_params`: The query parameters
        :param `extra_headers`: The extra headers
        :type `route_prefix`: `str`
        :type `route`: `str`
        :type `method`: `str`
        :type `url_params`: `dict`
        :type `json_params`: `dict`
        :type `data_params`: `dict`
        :type `query_params`: `dict`
        :type `extra_headers`: `dict`
        :return: The response
        :rtype: `dict`
        """
        # Form URL
        url: str = urljoin(
            route_prefix,
            route.format(**url_params) if url_params else route,
        )

        # Headers
        headers: dict[str, str] = extra_headers if extra_headers else {}
        if self.api_session_key:
            # Set authorization header
            headers["Authorization"] = f"{self.api_session_key}"

        logger.debug(
            f"Request: {method} {url} {query_params} {json_params} {data_params} {headers}"
        ) if self._logging else None

        try:
            r: Response = self._req_sess.request(
                method=method,
                url=url,
                json=json_params,
                data=data_params,
                params=query_params,
                headers=headers,
                verify=True,
                allow_redirects=True,
                timeout=self._timeout,
                proxies=self._proxies,
                stream=True,
            )
        except Exception as e:
            # Raise requests exceptions
            raise e

        logger.debug(
            f"Response: {r.status_code} {r.content}"
        ) if self._logging else None

        # Take action based on content type
        if "application/json" in r.headers["content-type"]:
            try:
                data: dict[str, Any] = r.json()
            except Exception:
                raise Exception(f"Couldn't parse JSON response: {r.content}")
        elif "text/csv" in r.headers["content-type"]:
            try:
                data = {
                    "data": (line.decode('utf-8') for line in r.iter_lines())
                }
            except Exception:
                raise Exception(f"Couldn't parse CSV response: {r.content}")
        else:
            raise Exception(
                f"Unknown Content-Type ({r.headers['content-type']}): ({r.content})"
            )

        if "status" in data:
            if data["status"] == "ERROR":
                if (
                    self.session_expired_callback
                    and "Session Expired" in data["message"]
                ):
                    self.session_expired_callback()
                    logger.debug(
                        "Session expired. Callback called"
                    ) if self._logging else None
                else:
                    raise Exception(f"Error: {data}")
            elif (
                data["status"] == "SUCCESS"
                and r.request.url == f"{self.base_url}/sliceorder"
            ):
                for order in data["orders"]:
                    if order["status"] == "ERROR":
                        raise Exception(f"Error: {data}")

        return data
