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

from typing import Any

from pytest import FixtureRequest, Parser, fixture

from integrate import ConnectToIntegrate, IntegrateData, IntegrateOrders
from integrate.ws import IntegrateWebSocket


def pytest_addoption(parser: Parser) -> None:
    """
    Add args from command line.

    :param parser: pytest parser
    :type parser: Parser
    :return: None
    """
    parser.addoption("--apiToken", action="store", default="integration_test")
    parser.addoption("--apiSecret", action="store", default="integration_test")
    parser.addoption("--totp", action="store", default="integration_test")
    parser.addoption("--loginUrl", action="store", default="integration_test")
    parser.addoption("--baseUrl", action="store", default="integration_test")
    parser.addoption("--socketUrl", action="store", default="integration_test")
    parser.addoption("--uid", action="store", default="integration_test")
    parser.addoption("--actid", action="store", default="integration_test")
    parser.addoption(
        "--apiSessionKey", action="store", default="integration_test"
    )
    parser.addoption(
        "--wsSessionKey", action="store", default="integration_test"
    )


@fixture(scope="session")
def c2i(request: FixtureRequest) -> ConnectToIntegrate:
    """
    Initialize ConnectToIntegrate object.

    :param fixture_request: pytest fixture request
    :type fixture_request: FixtureRequest
    :return: ConnectToIntegrate object
    """
    api_token: Any = request.config.getoption("--apiToken")
    api_secret: Any = request.config.getoption("--apiSecret")
    totp: Any = request.config.getoption(name="--totp")
    login_url: Any = request.config.getoption(name="--loginUrl")
    base_url: Any = request.config.getoption(name="--baseUrl")
    uid: Any = request.config.getoption(name="--uid")
    actid: Any = request.config.getoption(name="--actid")
    api_session_key: Any = request.config.getoption(name="--apiSessionKey")
    ws_session_key: Any = request.config.getoption(name="--wsSessionKey")

    if (
        uid != "integration_test"
        and actid != "integration_test"
        and api_session_key != "integration_test"
        and ws_session_key != "integration_test"
    ):
        c2i = ConnectToIntegrate(
            login_url=login_url if login_url != "integration_test" else None,
            base_url=base_url if base_url != "integration_test" else None,
        )
        c2i.set_session_keys(
            uid=uid,
            actid=actid,
            api_session_key=api_session_key,
            ws_session_key=ws_session_key,
        )
        return c2i

    if (
        api_token == "integration_test"  # nosec: B105
        or api_secret == "integration_test"  # nosec: B105
    ):
        raise ValueError(
            "Invalid uid or actid or api_session_key or ws_session_key or api_token or api_secret"
        )

    c2i = ConnectToIntegrate(
        login_url=login_url if login_url != "integration_test" else None,
        base_url=base_url if base_url != "integration_test" else None,
    )
    c2i.login(
        api_token=api_token,
        api_secret=api_secret,
        totp=totp if totp != "integration_test" else None,
    )
    print(
        f"\nAPI Session Key: {c2i.api_session_key}\nWS Session Key: {c2i.ws_session_key}"
    )
    return c2i


@fixture(scope="session")
def io(c2i: ConnectToIntegrate) -> IntegrateOrders:
    """
    Initialize IntegrateOrders object.

    :param c2i: ConnectToIntegrate object
    :return: IntegrateOrders object
    """
    io = IntegrateOrders(connect_to_integrate=c2i)
    return io


@fixture(scope="session")
def ic(c2i: ConnectToIntegrate) -> IntegrateData:
    """
    Initialize IntegrateData object.

    :param c2i: ConnectToIntegrate object
    :return: IntegrateData object
    """
    ic = IntegrateData(connect_to_integrate=c2i)
    return ic


@fixture(scope="session")
def iwebsocket(
    c2i: ConnectToIntegrate, request: FixtureRequest
) -> IntegrateWebSocket:
    """
    Initialize IntegrateWebSocket object.

    :param c2i: ConnectToIntegrate object
    :return: IntegrateWebSocket object
    """
    socket_url: Any = request.config.getoption(name="--socketUrl")

    iws = IntegrateWebSocket(connect_to_integrate=c2i)
    iws._socket_url = socket_url if socket_url != "integration_test" else iws._socket_url  # type: ignore
    return iws
