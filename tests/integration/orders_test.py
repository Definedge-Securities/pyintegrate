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
This module contains integration tests for IntegrateOrders class.
"""

from datetime import datetime
from time import sleep
from typing import Any

from pytest import raises

from integrate import IntegrateOrders
from integrate.connect import ConnectToIntegrate
from integrate.data import IntegrateData
from tests.responses_helper import compare_keys


def custom_order_placement(
    c2i: ConnectToIntegrate,
    io: IntegrateOrders,
    ic: IntegrateData,
    exchange: str,
    order_type: str,
    price_type: str,
    product_type: str,
    quantity: int,
    tradingsymbol: str,
    price: str = "ltp",
    trigger_price: str = "ltp",
) -> dict[str, Any]:
    """
    Custom order placement using ltp or lower_circuit/upper_circuit.

    :param `c2i`: `ConnectToIntegrate` object
    :param `io`: `IntegrateOrders` object
    :param `ic`: `IntegrateData` object
    :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
    :param `order_type`: Order type. Valid values are BUY, SELL.
    :param `price_type`: Price type. Valid values are MARKET, LIMIT, SL-MARKET, SL-LIMIT.
    :param `product_type`: Product type. Valid values are CNC, INTRADAY, NORMAL.
    :param `quantity`: Quantity to transact.
    :param `tradingsymbol`: Trading symbol of security to transact.
    :param `price`: Price at which order is to be placed. Not required for market orders.
    :param `trigger_price`: Trigger price for the order (Applicable only for price_type, SL-MARKET or SL-LIMIT).
    :type `c2i`: `ConnectToIntegrate`
    :type `io`: `IntegrateOrders`
    :type `ic`: `IntegrateData`
    :type `exchange`: `str`
    :type `order_type`: `str`
    :type `price_type`: `str`
    :type `product_type`: `str`
    :type `quantity`: `int`
    :type `tradingsymbol`: `str`
    :type `price`: `float`
    :type `trigger_price`: `float`
    :return: The order status
    :rtype: `dict[str, Any]`
    """

    price_diff_percentage: float = 0.1
    quote: dict[str, Any] = ic.quotes(
        exchange=exchange, trading_symbol=tradingsymbol
    )
    order: dict[str, Any] = {}

    if price_type == c2i.PRICE_TYPE_MARKET:
        order = io.place_order(
            exchange=exchange,
            order_type=order_type,
            price=0,
            price_type=price_type,
            product_type=product_type,
            quantity=quantity,
            tradingsymbol=tradingsymbol,
        )
    elif price_type == c2i.PRICE_TYPE_LIMIT:
        price_value: float = (
            float(quote["ltp"]) - (float(quote["ltp"]) * price_diff_percentage)
            if price == "ltp"
            else float(quote["lower_circuit"]) + 2
        )
        order = io.place_order(
            exchange=exchange,
            order_type=order_type,
            price=price_value,
            price_type=price_type,
            product_type=product_type,
            quantity=quantity,
            tradingsymbol=tradingsymbol,
        )
    elif price_type == c2i.PRICE_TYPE_SL_MKT:
        trigger_price_value: float = (
            float(quote["ltp"]) + (float(quote["ltp"]) * price_diff_percentage)
            if trigger_price == "ltp"
            else float(quote["upper_circuit"]) - 2
        )
        order = io.place_order(
            exchange=exchange,
            order_type=order_type,
            price=0,
            price_type=price_type,
            product_type=product_type,
            quantity=quantity,
            tradingsymbol=tradingsymbol,
            trigger_price=trigger_price_value,
        )
    elif price_type == c2i.PRICE_TYPE_SL_LMT:
        trigger_price_value = (
            float(quote["ltp"]) + (float(quote["ltp"]) * price_diff_percentage)
            if trigger_price == "ltp"
            else float(quote["upper_circuit"]) - 2
        )
        price_value = (
            trigger_price_value - (trigger_price_value * price_diff_percentage)
            if price == "ltp"
            else float(quote["lower_circuit"]) + 2
        )
        order = io.place_order(
            exchange=exchange,
            order_type=order_type,
            price=price_value,
            price_type=price_type,
            product_type=product_type,
            quantity=quantity,
            tradingsymbol=tradingsymbol,
            trigger_price=trigger_price_value,
        )

    assert isinstance(order, dict)
    assert compare_keys("place_order.json", order)

    sleep(1)
    placed_orders: dict[str, Any] = io.orders()
    placed_order: dict[str, Any] = next(
        ord
        for ord in placed_orders["orders"]
        if ord["order_id"] == order["order_id"]
    )
    return placed_order


def close_open_positions_and_cancel_open_orders(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Close all open positions and cancel open orders.

    :param `c2i`: `ConnectToIntegrate` object
    :param `io`: `IntegrateOrders` object
    :type `c2i`: `ConnectToIntegrate`
    :type `io`: `IntegrateOrders`
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.orders()
        for order in orders["orders"]:
            if order["status"] == io.ORDER_STATUS_OPEN:
                io.cancel_order(order_id=order["order_id"])
        assert "No Orders Found" in str(e.value)

    with raises(Exception) as e:
        positions: dict[str, Any] = io.positions()
        for position in positions["positions"]:
            if int(position["day_buy_qty"]) > 0:
                placed_order: dict[str, Any] = custom_order_placement(
                    c2i=c2i,
                    io=io,
                    ic=ic,
                    exchange=position["exchange"],
                    order_type=c2i.ORDER_TYPE_SELL,
                    price_type=c2i.PRICE_TYPE_MARKET,
                    product_type=c2i.PRODUCT_TYPE_INTRADAY,
                    quantity=int(position["day_buy_qty"]),
                    tradingsymbol=position["tradingsymbol"],
                )
                assert isinstance(placed_order, dict)
                assert placed_order["order_status"] == io.ORDER_STATUS_COMPLETE
            elif int(position["day_sell_qty"]) > 0:
                placed_order = custom_order_placement(
                    c2i=c2i,
                    io=io,
                    ic=ic,
                    exchange=position["exchange"],
                    order_type=c2i.ORDER_TYPE_BUY,
                    price_type=c2i.PRICE_TYPE_MARKET,
                    product_type=c2i.PRODUCT_TYPE_INTRADAY,
                    quantity=int(position["day_sell_qty"]),
                    tradingsymbol=position["tradingsymbol"],
                )
                assert isinstance(placed_order, dict)
                assert placed_order["order_status"] == io.ORDER_STATUS_COMPLETE
        assert "No Positions Found" in str(e.value)


def test_placing_market_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test placing an order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    close_open_positions_and_cancel_open_orders(c2i=c2i, io=io, ic=ic)

    placed_order: dict[str, Any] = custom_order_placement(
        c2i=c2i,
        io=io,
        ic=ic,
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price_type=c2i.PRICE_TYPE_MARKET,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1,
        tradingsymbol="SBIN-EQ",
    )
    assert isinstance(placed_order, dict)
    assert placed_order["order_status"] in io.order_statuses
    close_open_positions_and_cancel_open_orders(c2i=c2i, io=io, ic=ic)


def test_placing_limit_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test placing a limit order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    placed_order: dict[str, Any] = custom_order_placement(
        c2i=c2i,
        io=io,
        ic=ic,
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price_type=c2i.PRICE_TYPE_LIMIT,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1,
        tradingsymbol="SBIN-EQ",
        price="ltp",
    )
    assert isinstance(placed_order, dict)
    assert placed_order["order_status"] in io.order_statuses
    close_open_positions_and_cancel_open_orders(c2i=c2i, io=io, ic=ic)


def test_modifying_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test modifying an order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    placed_order: dict[str, Any] = custom_order_placement(
        c2i=c2i,
        io=io,
        ic=ic,
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price_type=c2i.PRICE_TYPE_LIMIT,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1,
        tradingsymbol="SBIN-EQ",
        price="lower_circuit",
    )
    assert isinstance(placed_order, dict)
    if placed_order["order_status"] == io.ORDER_STATUS_OPEN:
        order1: dict[str, Any] = io.modify_order(
            exchange=c2i.EXCHANGE_TYPE_NSE,
            order_id=placed_order["order_id"],
            order_type=c2i.ORDER_TYPE_BUY,
            price=0,
            price_type=c2i.PRICE_TYPE_MARKET,
            product_type=c2i.PRODUCT_TYPE_INTRADAY,
            quantity=1,
            tradingsymbol="SBIN-EQ",
        )
        assert isinstance(order1, dict)
        assert compare_keys("modify_order.json", order1)

        sleep(1)
        with raises(Exception) as e:
            placed_orders: dict[str, Any] = io.orders()
            placed_order1: dict[str, Any] = next(
                ord
                for ord in placed_orders["orders"]
                if ord["order_id"] == order1["order_id"]
            )
            assert placed_order1["order_status"] in io.order_statuses
            close_open_positions_and_cancel_open_orders(c2i=c2i, io=io, ic=ic)
            assert "No Orders Found" in str(e.value)


def test_cancelling_order(io: IntegrateOrders) -> None:
    """
    Test cancelling an order.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.orders()
        for order in orders["orders"]:
            if order["status"] == io.ORDER_STATUS_OPEN:
                io.cancel_order(order_id=order["order_id"])
        assert "No Orders Found" in str(e.value)


def test_slicing_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test slicing an order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    orders: dict[str, Any] = io.slice_order(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price=0,
        price_type=c2i.PRICE_TYPE_MARKET,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1000,
        slices=4,
        tradingsymbol="SBIN-EQ",
    )
    assert isinstance(orders, dict)
    assert compare_keys("slice_order.json", orders)

    sleep(1)
    with raises(Exception) as e:
        placed_orders: dict[str, Any] = io.orders()
        for order in orders["orders"]:
            placed_order: dict[str, Any] = next(
                ord
                for ord in placed_orders["orders"]
                if ord["order_id"] == order["order_id"]
            )
            assert placed_order["order_status"] in io.order_statuses
            close_open_positions_and_cancel_open_orders(c2i=c2i, io=io, ic=ic)
            assert "No Orders Found" in str(e.value)


def test_product_type_conversion(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test converting an open position's product type.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    placed_order: dict[str, Any] = custom_order_placement(
        c2i=c2i,
        io=io,
        ic=ic,
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price_type=c2i.PRICE_TYPE_MARKET,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1,
        tradingsymbol="SBIN-EQ",
    )
    assert isinstance(placed_order, dict)
    assert placed_order["order_status"] in io.order_statuses
    with raises(Exception) as e:
        positions: dict[str, Any] = io.positions()
        for position in positions["positions"]:
            if (
                position["tradingsymbol"] == "SBIN-EQ"
                and position["product_type"] == c2i.PRODUCT_TYPE_INTRADAY
                and position["day_buy_qty"] == "1"
            ):
                order: dict[str, Any] = io.convert_position_product_type(
                    exchange=position["exchange"],
                    order_type=c2i.ORDER_TYPE_BUY,
                    prev_product=position["product_type"],
                    product_type=c2i.PRODUCT_TYPE_CNC,
                    quantity=int(position["day_buy_qty"]),
                    tradingsymbol=position["tradingsymbol"],
                )
                assert isinstance(order, dict)
                assert "status" in order
                assert order["status"] == "SUCCESS"
                close_open_positions_and_cancel_open_orders(
                    c2i=c2i, io=io, ic=ic
                )
        assert "No Positions Found" in str(e.value)


def test_placing_gtt_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test placing a GTT order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    exchange: str = c2i.EXCHANGE_TYPE_NSE
    order_type: str = c2i.ORDER_TYPE_BUY
    tradingsymbol: str = "SBIN-EQ"
    quantity: int = 1
    price_diff_percentage: float = 0.1
    quote: dict[str, Any] = ic.quotes(
        exchange=exchange, trading_symbol=tradingsymbol
    )
    alert_price_value: float = float(quote["ltp"]) + (
        float(quote["ltp"]) * price_diff_percentage
    )
    price_value: float = alert_price_value - (
        alert_price_value * price_diff_percentage
    )

    order: dict[str, Any] = io.place_gtt_order(
        exchange=exchange,
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert compare_keys("place_gtt_order.json", order)
    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_gtt_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_modifying_gtt_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test modifying a GTT order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    exchange: str = c2i.EXCHANGE_TYPE_NSE
    order_type: str = c2i.ORDER_TYPE_BUY
    tradingsymbol: str = "SBIN-EQ"
    quantity: int = 1
    price_diff_percentage: float = 0.1
    quote: dict[str, Any] = ic.quotes(
        exchange=exchange, trading_symbol=tradingsymbol
    )

    alert_price_value: float = float(quote["ltp"]) + (
        float(quote["ltp"]) * price_diff_percentage
    )
    price_value: float = alert_price_value - (
        alert_price_value * price_diff_percentage
    )
    order: dict[str, Any] = io.place_gtt_order(
        exchange=exchange,
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert compare_keys("place_gtt_order.json", order)
    order1: dict[str, Any] = io.modify_gtt_order(
        exchange=exchange,
        alert_id=order["alert_id"],
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert isinstance(order1, dict)
    assert compare_keys("modify_gtt_order.json", order1)

    sleep(1)
    with raises(Exception) as e:
        placed_orders: dict[str, Any] = io.gtt_orders()
        placed_order1: dict[str, Any] = next(
            ord
            for ord in placed_orders["pendingGTTOrderBook"]
            if ord["alert_id"] == order1["alert_id"]
        )
        assert placed_order1["alert_id"] == order1["alert_id"]
        assert "No Orders Found" in str(e.value)

    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_gtt_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_cancelling_gtt_order(io: IntegrateOrders) -> None:
    """
    Test cancelling a GTT order.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_gtt_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_placing_oco_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test placing a OCO order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    exchange: str = c2i.EXCHANGE_TYPE_NSE
    order_type: str = c2i.ORDER_TYPE_BUY
    tradingsymbol: str = "SBIN-EQ"
    quantity: int = 1
    price_diff_percentage: float = 0.1
    quote: dict[str, Any] = ic.quotes(
        exchange=exchange, trading_symbol=tradingsymbol
    )
    alert_price_value: float = float(quote["ltp"]) + (
        float(quote["ltp"]) * price_diff_percentage
    )
    price_value: float = alert_price_value - (
        alert_price_value * price_diff_percentage
    )

    order: dict[str, Any] = io.place_gtt_order(
        exchange=exchange,
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert compare_keys("place_gtt_order.json", order)
    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_gtt_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_modifying_oco_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test modifying an OCO order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :param ic: IntegrateData object
    :type c2i: ConnectToIntegrate
    :type io: IntegrateOrders
    :type ic: IntegrateData
    :return: None
    """
    exchange: str = c2i.EXCHANGE_TYPE_NSE
    order_type: str = c2i.ORDER_TYPE_BUY
    tradingsymbol: str = "SBIN-EQ"
    quantity: int = 1
    price_diff_percentage: float = 0.1
    quote: dict[str, Any] = ic.quotes(
        exchange=exchange, trading_symbol=tradingsymbol
    )

    alert_price_value: float = float(quote["ltp"]) + (
        float(quote["ltp"]) * price_diff_percentage
    )
    price_value: float = alert_price_value - (
        alert_price_value * price_diff_percentage
    )
    order: dict[str, Any] = io.place_gtt_order(
        exchange=exchange,
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert compare_keys("place_gtt_order.json", order)
    order1: dict[str, Any] = io.modify_gtt_order(
        exchange=exchange,
        alert_id=order["alert_id"],
        order_type=order_type,
        price=price_value,
        quantity=quantity,
        tradingsymbol=tradingsymbol,
        alert_price=alert_price_value,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    assert isinstance(order1, dict)
    assert compare_keys("modify_gtt_order.json", order1)

    sleep(1)
    with raises(Exception) as e:
        placed_orders: dict[str, Any] = io.gtt_orders()
        placed_order1: dict[str, Any] = next(
            ord
            for ord in placed_orders["pendingGTTOrderBook"]
            if ord["alert_id"] == order1["alert_id"]
        )
        assert placed_order1["alert_id"] == order1["alert_id"]
        assert "No Orders Found" in str(e.value)

    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_gtt_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_cancelling_oco_order(io: IntegrateOrders) -> None:
    """
    Test cancelling an OCO order.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        for order in orders["pendingGTTOrderBook"]:
            io.cancel_oco_order(alert_id=order["alert_id"])
        assert "No GTT Order Found" in str(e.value)


def test_fetching_orders(io: IntegrateOrders) -> None:
    """
    Test fetching orders.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.orders()
        assert isinstance(orders, dict)
        assert "orders" in orders
        assert (
            orders["orders"] != []
            if len(orders["orders"])
            else orders["orders"] == []
        )
        assert (
            compare_keys("orders.json", orders)
            if len(orders["orders"])
            else True
        )
        assert "No Orders Found" in str(e.value)


def test_fetching_order_status(
    c2i: ConnectToIntegrate, io: IntegrateOrders, ic: IntegrateData
) -> None:
    """
    Test fetching order status.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    placed_order: dict[str, Any] = custom_order_placement(
        c2i=c2i,
        io=io,
        ic=ic,
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price_type=c2i.PRICE_TYPE_LIMIT,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=1,
        tradingsymbol="SBIN-EQ",
        price="lower_circuit",
    )
    assert isinstance(placed_order, dict)
    order: dict[str, Any] = io.order(order_id=placed_order["order_id"])
    assert isinstance(order, dict)
    assert "order_id" in order
    assert order["order_id"] == placed_order["order_id"]
    print(order)
    assert compare_keys("order.json", order) if "order_id" in order else True


def test_fetching_gtt_orders(io: IntegrateOrders) -> None:
    """
    Test fetching GTT orders.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        orders: dict[str, Any] = io.gtt_orders()
        assert isinstance(orders, dict)
        assert "pendingGTTOrderBook" in orders
        assert (
            orders["pendingGTTOrderBook"] != []
            if len(orders["pendingGTTOrderBook"])
            else orders["pendingGTTOrderBook"] == []
        )
        assert (
            compare_keys("gtt_orders.json", orders)
            if len(orders["pendingGTTOrderBook"])
            else True
        )
        assert "No GTT Order Found" in str(e.value)


def test_fetching_trades(io: IntegrateOrders) -> None:
    """
    Test fetching trades.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        trades: dict[str, Any] = io.trades()
        assert isinstance(trades, dict)
        assert "trades" in trades
        assert (
            trades["trades"] != []
            if len(trades["trades"])
            else trades["trades"] == []
        )
        assert (
            compare_keys("trades.json", trades)
            if len(trades["trades"])
            else True
        )
        assert "No Trades Found" in str(e.value)


def test_fetching_positions(io: IntegrateOrders) -> None:
    """
    Test fetching positions.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        positions: dict[str, Any] = io.positions()
        assert isinstance(positions, dict)
        assert "positions" in positions
        assert (
            positions["positions"] != []
            if len(positions["positions"])
            else positions["positions"] == []
        )
        assert (
            compare_keys("positions.json", positions)
            if len(positions["positions"])
            else True
        )
        assert "No Positions Found" in str(e.value)


def test_fetching_holdings(io: IntegrateOrders) -> None:
    """
    Test fetching holdings.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    with raises(Exception) as e:
        holdings: dict[str, Any] = io.holdings()
        assert isinstance(holdings, dict)
        assert "data" in holdings
        assert (
            holdings["data"] != []
            if len(holdings["data"])
            else holdings["data"] == []
        )
        assert (
            compare_keys("holdings.json", holdings)
            if len(holdings["data"])
            else True
        )
        assert "No Holdings Found" in str(e.value)


def test_fetching_limits(io: IntegrateOrders) -> None:
    """
    Test fetching limits.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    limits: dict[str, Any] = io.limits()
    assert isinstance(limits, dict)
    assert compare_keys("limits.json", limits)


def test_fetching_margins(io: IntegrateOrders) -> None:
    """
    Test fetching margins.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    margins: dict[str, Any] = io.margins(
        orders=[
            {
                "exchange": io.c2i.EXCHANGE_TYPE_NSE,
                "tradingsymbol": "SBIN-EQ",
                "quantity": 50,
                "price": 0,
                "product_type": io.c2i.PRODUCT_TYPE_INTRADAY,
                "order_type": io.c2i.ORDER_TYPE_BUY,
                "price_type": io.c2i.PRICE_TYPE_MARKET,
            }
        ]
    )
    assert isinstance(margins, dict)
    assert compare_keys("margins.json", margins)


def test_span_calculation(io: IntegrateOrders) -> None:
    """
    Test span calculation.

    :param io: IntegrateOrders object
    :type io: IntegrateOrders
    :return: None
    """
    strike: int = 19700
    expiry: datetime = datetime(2023, 8, 31)
    if expiry < datetime.today():
        raise Exception("Expiry date is in the past")

    span: dict[str, Any] = io.span_calculator(
        positions=[
            {
                "product_type": io.c2i.PRODUCT_TYPE_INTRADAY,
                "exchange": io.c2i.EXCHANGE_TYPE_NFO,
                "symbol_name": "NIFTY",
                "tradingsymbol": f"NIFTY{expiry.strftime('%d%b%Y').upper()}{strike}C",
                "expiry": f"{expiry.strftime('%d-%b-%Y').upper()}",
                "open_sell_qty": 100,
                "open_buy_qty": 0,
                "option_strike": strike,
                "option_type": "CE",
            },
            {
                "product_type": io.c2i.PRODUCT_TYPE_NORMAL,
                "exchange": io.c2i.EXCHANGE_TYPE_NFO,
                "symbol_name": "NIFTY",
                "tradingsymbol": f"NIFTY{expiry.strftime('%d%b%Y').upper()}{strike}P",
                "expiry": f"{expiry.strftime('%d-%b-%Y').upper()}",
                "open_sell_qty": 100,
                "open_buy_qty": 0,
                "option_strike": strike,
                "option_type": "PE",
            },
        ]
    )
    assert isinstance(span, dict)
    assert compare_keys("span_calculator.json", span)
