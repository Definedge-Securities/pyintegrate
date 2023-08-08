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
This module contains functions that configure pytest for unit tests.
"""

from pytest import fixture

from integrate import ConnectToIntegrate, IntegrateData, IntegrateOrders
from integrate.ws import IntegrateWebSocketClientProtocol


@fixture(scope="session")
def c2i() -> ConnectToIntegrate:
    """
    Initialize ConnectToIntegrate object.

    :return: ConnectToIntegrate object
    """
    c2i = ConnectToIntegrate(
        login_url="http://signin-defsec-unit-test",
        base_url="http://integrate-defsec-unit-test/",
    )
    c2i.set_session_keys(
        uid="unit_test",
        actid="unit_test",
        api_session_key="unit_test",
        ws_session_key="unit_test",
    )
    return c2i


@fixture(scope="session")
def c2i_with_logging() -> ConnectToIntegrate:
    """
    Initialize ConnectToIntegrate object with logging.

    :return: ConnectToIntegrate object
    """
    c2i = ConnectToIntegrate(
        login_url="http://signin-defsec-unit-test",
        base_url="http://integrate-defsec-unit-test/",
        logging=True,
    )
    c2i.set_session_keys(
        uid="unit_test",
        actid="unit_test",
        api_session_key="unit_test",
        ws_session_key="unit_test",
    )
    return c2i


@fixture(scope="session")
def io(c2i_with_logging: ConnectToIntegrate) -> IntegrateOrders:
    """
    Initialize IntegrateOrders object.

    :param c2i_with_logging: ConnectToIntegrate object
    :return: IntegrateOrders object
    """
    io = IntegrateOrders(connect_to_integrate=c2i_with_logging)
    return io


@fixture(scope="session")
def ic(c2i_with_logging: ConnectToIntegrate) -> IntegrateData:
    """
    Initialize IntegrateData object.

    :param c2i_with_logging: ConnectToIntegrate object
    :return: IntegrateData object
    """
    ic = IntegrateData(connect_to_integrate=c2i_with_logging)
    return ic


@fixture(scope="session")
def iwsproto() -> IntegrateWebSocketClientProtocol:
    """
    Initialize IntegrateWebSocketClientProtocol object.

    :return: IntegrateWebSocketClientProtocol object
    """
    from autobahn.testutil import FakeTransport  # type: ignore
    from autobahn.wamp.types import TransportDetails  # type: ignore

    from integrate.ws import (
        IntegrateWebSocketClientFactory,
        IntegrateWebSocketClientProtocol,
    )

    t = FakeTransport()
    f = IntegrateWebSocketClientFactory()
    p = IntegrateWebSocketClientProtocol()
    p.factory = f
    p.transport = t  # type: ignore
    p._transport_details = TransportDetails()  # type: ignore

    p.connectionMade()  # type: ignore
    p.state = p.STATE_OPEN
    p.websocket_version = 18
    return p
