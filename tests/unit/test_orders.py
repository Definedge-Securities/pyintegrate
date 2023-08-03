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
from urllib.parse import urljoin

from responses import GET, POST, activate, add

from integrate import ConnectToIntegrate, IntegrateOrders
from tests.responses_helper import get_mock_response


@activate
def test_placing_order(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test placing an order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the place order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "placeorder",
        ),
        body=get_mock_response("place_order.json"),
        content_type="application/json",
    )
    # Place order
    order: dict[str, Any] = io.place_order(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        order_type=c2i.ORDER_TYPE_SELL,
        price=0,
        price_type=c2i.PRICE_TYPE_MARKET,
        product_type=c2i.PRODUCT_TYPE_NORMAL,
        quantity=50,
        tradingsymbol="NIFTY23FEB23F",
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "order_id" in order


@activate
def test_modifying_order(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test modifying an open order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the modify order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "modify",
        ),
        body=get_mock_response("modify_order.json"),
        content_type="application/json",
    )
    # Modify order
    order: dict[str, Any] = io.modify_order(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        order_id="1234567890000",
        order_type=c2i.ORDER_TYPE_SELL,
        price=17500,
        price_type=c2i.PRICE_TYPE_LIMIT,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=100,
        tradingsymbol="NIFTY23FEB23F",
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "order_id" in order


@activate
def test_cancelling_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test cancelling an open order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    order_id: str = "1234567890012"
    # Add a mock response for the cancel order endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"cancel/{order_id}",
        ),
        body=get_mock_response("cancel_order.json"),
        content_type="application/json",
    )
    # Cancel order
    order: dict[str, Any] = io.cancel_order(
        order_id=order_id,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "order_id" in order


@activate
def test_slicing_order(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test slicing an order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the slice order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "sliceorder",
        ),
        body=get_mock_response("slice_order.json"),
        content_type="application/json",
    )
    # Slice order
    order: dict[str, Any] = io.slice_order(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        order_type=c2i.ORDER_TYPE_BUY,
        price=17600,
        price_type=c2i.PRICE_TYPE_LIMIT,
        product_type=c2i.PRODUCT_TYPE_NORMAL,
        quantity=1000,
        slices=2,
        tradingsymbol="NIFTY23FEB23F",
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "orders" in order
    assert "status" in order["orders"][0]
    assert "order_id" in order["orders"][0]


@activate
def test_product_type_conversion(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test converting an open position's product type.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the product conversion endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "productconversion",
        ),
        body=get_mock_response("product_conversion.json"),
        content_type="application/json",
    )
    # Convert product type
    order: dict[str, Any] = io.convert_position_product_type(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        order_type=c2i.ORDER_TYPE_SELL,
        prev_product=c2i.PRODUCT_TYPE_NORMAL,
        product_type=c2i.PRODUCT_TYPE_INTRADAY,
        quantity=50,
        tradingsymbol="NIFTY23FEB23F",
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order


@activate
def test_placing_gtt_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test placing a GTT order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the place GTT order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "gttplaceorder",
        ),
        body=get_mock_response("place_gtt_order.json"),
        content_type="application/json",
    )
    # Place GTT order
    order: dict[str, Any] = io.place_gtt_order(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        order_type=c2i.ORDER_TYPE_BUY,
        price=3100,
        quantity=1,
        tradingsymbol="TCS-EQ",
        alert_price=3100,
        condition=c2i.GTT_CONDITION_LTP_BELOW,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_modifying_gtt_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test modifying an open GTT order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the modify GTT order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "gttmodify",
        ),
        body=get_mock_response("modify_gtt_order.json"),
        content_type="application/json",
    )
    # Modify GTT order
    order: dict[str, Any] = io.modify_gtt_order(
        exchange=c2i.EXCHANGE_TYPE_NSE,
        alert_id="1234001",
        order_type=c2i.ORDER_TYPE_BUY,
        price=3390,
        quantity=3,
        tradingsymbol="TCS-EQ",
        alert_price=3390,
        condition=c2i.GTT_CONDITION_LTP_ABOVE,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_cancelling_gtt_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test cancelling an open GTT order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    alert_id: str = "1234001"
    # Add a mock response for the cancel GTT order endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"gttcancel/{alert_id}",
        ),
        body=get_mock_response("cancel_gtt_order.json"),
        content_type="application/json",
    )
    # Cancel GTT order
    order: dict[str, Any] = io.cancel_gtt_order(
        alert_id=alert_id,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_placing_oco_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test placing an OCO order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the place OCO order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "ocoplaceorder",
        ),
        body=get_mock_response("place_oco_order.json"),
        content_type="application/json",
    )
    # Place OCO order
    order: dict[str, Any] = io.place_oco_order(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        order_type=c2i.ORDER_TYPE_SELL,
        tradingsymbol="NIFTY29MAR23F",
        stoploss_quantity=50,
        stoploss_price=17300,
        target_quantity=50,
        target_price=17000,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_modifying_oco_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test modifying an open OCO order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the modify OCO order endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "ocomodify",
        ),
        body=get_mock_response("modify_oco_order.json"),
        content_type="application/json",
    )
    # Modify OCO order
    order: dict[str, Any] = io.modify_oco_order(
        exchange=c2i.EXCHANGE_TYPE_NFO,
        alert_id="1234002",
        order_type=c2i.ORDER_TYPE_SELL,
        tradingsymbol="NIFTY29MAR23F",
        stoploss_quantity=100,
        stoploss_price=17250,
        target_quantity=100,
        target_price=17050,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_cancelling_oco_order(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test cancelling an open OCO order.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    alert_id: str = "1234002"
    # Add a mock response for the cancel OCO order endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"ococancel/{alert_id}",
        ),
        body=get_mock_response("cancel_oco_order.json"),
        content_type="application/json",
    )
    # Cancel OCO order
    order: dict[str, Any] = io.cancel_oco_order(
        alert_id=alert_id,
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "status" in order
    assert "alert_id" in order


@activate
def test_fetching_orders(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test fetching orders.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the orders endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "orders",
        ),
        body=get_mock_response("orders.json"),
        content_type="application/json",
    )
    # Fetch orders
    orders: dict[str, Any] = io.orders()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(orders, dict)
    assert "orders" in orders
    assert "order_id" in orders["orders"][0]
    assert "tradingsymbol" in orders["orders"][0]
    assert "order_status" in orders["orders"][0]


@activate
def test_fetching_order_status(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test fetching order status.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    order_id: str = "23072600000002"
    # Add a mock response for the order status endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            f"order/{order_id}",
        ),
        body=get_mock_response("order.json"),
        content_type="application/json",
    )
    # Fetch order status
    order: dict[str, Any] = io.order(order_id=order_id)
    # Assert that the response is a dict and contains the required keys
    assert isinstance(order, dict)
    assert "order_id" in order
    assert "tradingsymbol" in order
    assert "order_status" in order


@activate
def test_fetching_gtt_orders(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test fetching GTT orders.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the GTT orders endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "gttorders",
        ),
        body=get_mock_response("gtt_orders.json"),
        content_type="application/json",
    )
    # Fetch GTT orders
    orders: dict[str, Any] = io.gtt_orders()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(orders, dict)
    assert "pendingGTTOrderBook" in orders
    assert "alert_id" in orders["pendingGTTOrderBook"][0]
    assert "tradingsymbol" in orders["pendingGTTOrderBook"][0]
    assert "quantity" in orders["pendingGTTOrderBook"][0]


@activate
def test_fetching_trades(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test fetching trades.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the trades endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "trades",
        ),
        body=get_mock_response("trades.json"),
        content_type="application/json",
    )
    # Fetch trades
    trades: dict[str, Any] = io.trades()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(trades, dict)
    assert "trades" in trades
    assert "order_id" in trades["trades"][0]
    assert "tradingsymbol" in trades["trades"][0]
    assert "exchange_orderid" in trades["trades"][0]


@activate
def test_fetching_positions(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test fetching positions.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the positions endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "positions",
        ),
        body=get_mock_response("positions.json"),
        content_type="application/json",
    )
    # Fetch positions
    positions: dict[str, Any] = io.positions()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(positions, dict)
    assert "positions" in positions
    assert "day_averageprice" in positions["positions"][0]
    assert "net_averageprice" in positions["positions"][0]


@activate
def test_fetching_holdings(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test fetching holdings.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the holdings endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "holdings",
        ),
        body=get_mock_response("holdings.json"),
        content_type="application/json",
    )
    # Fetch holdings
    holdings: dict[str, Any] = io.holdings()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(holdings, dict)
    assert "data" in holdings
    assert "tradingsymbol" in holdings["data"][0]
    assert "avg_buy_price" in holdings["data"][0]


@activate
def test_fetching_limits(c2i: ConnectToIntegrate, io: IntegrateOrders) -> None:
    """
    Test fetching limits.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the limits endpoint
    add(
        method=GET,
        url=urljoin(
            c2i.base_url,
            "limits",
        ),
        body=get_mock_response("limits.json"),
        content_type="application/json",
    )
    # Fetch limits
    limits: dict[str, Any] = io.limits()
    # Assert that the response is a dict and contains the required keys
    assert isinstance(limits, dict)
    assert "status" in limits
    assert "cash" in limits


@activate
def test_fetching_margins(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test fetching margins.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the margins endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "margin",
        ),
        body=get_mock_response("margins.json"),
        content_type="application/json",
    )
    # Fetch margins
    margins: dict[str, Any] = io.margins(
        orders=[
            {
                "exchange": c2i.EXCHANGE_TYPE_NFO,
                "tradingsymbol": "NIFTY23FEB23F",
                "quantity": 50,
                "price": 18000,
                "product_type": c2i.PRODUCT_TYPE_INTRADAY,
                "order_type": c2i.ORDER_TYPE_BUY,
                "price_type": c2i.PRICE_TYPE_LIMIT,
            }
        ]
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(margins, dict)
    assert "status" in margins
    assert "marginUsed" in margins
    assert "newTotalMarginUsed" in margins
    assert "newMarginUsedAfterTrade" in margins


@activate
def test_span_calculation(
    c2i: ConnectToIntegrate, io: IntegrateOrders
) -> None:
    """
    Test span calculation.

    :param c2i: ConnectToIntegrate object
    :param io: IntegrateOrders object
    :return: None
    """
    # Add a mock response for the span calculator endpoint
    add(
        method=POST,
        url=urljoin(
            c2i.base_url,
            "spancalculator",
        ),
        body=get_mock_response("span_calculator.json"),
        content_type="application/json",
    )
    # Calculate span
    span: dict[str, Any] = io.span_calculator(
        positions=[
            {
                "product_type": c2i.PRODUCT_TYPE_NORMAL,
                "exchange": c2i.EXCHANGE_TYPE_NFO,
                "symbol_name": "NIFTY",
                "tradingsymbol": "NIFTY23FEB2317700C",
                "expiry": "23-FEB-2023",
                "open_sell_qty": 100,
                "open_buy_qty": 0,
                "option_strike": 17700,
                "option_type": "CE",
            },
            {
                "product_type": c2i.PRODUCT_TYPE_NORMAL,
                "exchange": c2i.EXCHANGE_TYPE_NFO,
                "symbol_name": "NIFTY",
                "tradingsymbol": "NIFTY23FEB2317700P",
                "expiry": "23-FEB-2023",
                "open_sell_qty": 100,
                "open_buy_qty": 0,
                "option_strike": 17700,
                "option_type": "PE",
            },
        ]
    )
    # Assert that the response is a dict and contains the required keys
    assert isinstance(span, dict)
    assert "status" in span
    assert "span" in span
    assert "exposure" in span
