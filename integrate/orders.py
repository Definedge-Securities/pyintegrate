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
This module contains the IntegrateOrders class which is used to connect to
the Integrate Orders API and place orders, modify orders, cancel orders,
get order book, get order status, get trade book, get positions, convert
product type, place GTT order, modify GTT order, cancel GTT order.

Example:

.. code-block:: python

    from integrate import ConnectToIntegrate, IntegrateOrders

    c2i = ConnectToIntegrate()
    c2i.login(api_token="YOUR_API_TOKEN", api_secret="YOUR_API_SECRET")

    io = IntegrateOrders(c2i)
    io.place_order(
         exchange="NSE",
         order_type="BUY",
         price=0,
         price_type="MARKET",
         product_type="INTRADAY",
         quantity=1,
         tradingsymbol="ACC-EQ",
    )
    io.order(order_id="210630000000000")
    io.orders()
"""

from logging import DEBUG, Logger, getLogger
from typing import Any, Union

from integrate import ConnectToIntegrate

logger: Logger = getLogger(__name__)
logger.setLevel(DEBUG)


class IntegrateOrders:
    """
    Definedge Securities Integrate Orders API class

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
        self.order_statuses: list[str] = [
            self.c2i.ORDER_STATUS_NEW,
            self.c2i.ORDER_STATUS_OPEN,
            self.c2i.ORDER_STATUS_COMPLETE,
            self.c2i.ORDER_STATUS_CANCELLED,
            self.c2i.ORDER_STATUS_REJECTED,
            self.c2i.ORDER_STATUS_REPLACED,
        ]

    def place_order(  # noqa: C901
        self,
        exchange: str,
        order_type: str,
        price: float,
        price_type: str,
        product_type: str,
        quantity: int,
        tradingsymbol: str,
        amo: Union[str, None] = None,
        book_loss_price: Union[float, None] = None,
        book_profit_price: Union[float, None] = None,
        disclosed_quantity: Union[int, None] = None,
        market_protection: Union[float, None] = None,
        remarks: Union[str, None] = None,
        trailing_price: Union[float, None] = None,
        trigger_price: Union[float, None] = None,
        validity: str = "DAY",
    ) -> dict[str, Any]:
        """
        Place an order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `price`: Price at which order is to be placed. Should be 0 for MARKET order.
        :param `price_type`: Price type. Valid values are MARKET, LIMIT, SL-MARKET, SL-LIMIT.
        :param `product_type`: Product type. Valid values are CNC, INTRADAY, NORMAL.
        :param `quantity`: Quantity to transact.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `amo`: If set to True, AMO order will be placed. Defaults to False.
        :param `book_loss_price`: Book loss price (Applicable only for Bracket orders).
        :param `book_profit_price`: Book profit price (Applicable only for Bracket orders).
        :param `disclosed_quantity`: Disclosed quantity for the order (Only for Equity and MCX).
        :param `market_protection`: Market protection percentage for the order (only for BSE and MCX).
        :param `remarks`: Remarks for the order.
        :param `trailing_price`: Trailing price for the order (Applicable only High Leverage product and Bracket order).
        :param `trigger_price`: Trigger price for the order (Applicable only for price_type, SL-MARKET or SL-LIMIT).
        :param `validity`: Validity for the order. Valid values are DAY, IOC, EOS. Defaults to DAY.
        :type `exchange`: `str`
        :type `order_type`: `str`
        :type `price`: `float`
        :type `price_type`: `str`
        :type `product_type`: `str`
        :type `quantity`: `int`
        :type `tradingsymbol`: `str`
        :type `amo`: `str`
        :type `book_loss_price`: `float`
        :type `book_profit_price`: `float`
        :type `disclosed_quantity`: `int`
        :type `market_protection`: `float`
        :type `remarks`: `str`
        :type `trailing_price`: `float`
        :type `trigger_price`: `float`
        :type `validity`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if price_type not in self.c2i.price_types:
            raise ValueError("Invalid price type")

        if product_type not in self.c2i.product_types:
            raise ValueError("Invalid product type")

        if price_type == "MARKET" and price != 0:
            raise ValueError("Price should be 0 for market order")

        if price_type == "SL-LIMIT":
            if order_type == "BUY" and trigger_price and trigger_price > price:
                raise ValueError(
                    "Trigger price cannot be greater than price for SL-LIMIT BUY order"
                )
            elif (
                order_type == "SELL"
                and trigger_price
                and trigger_price < price
            ):
                raise ValueError(
                    "Trigger price cannot be lesser than price for SL-LIMIT SELL order"
                )

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="placeorder",
            method="POST",
            json_params=json_params,
        )

    def modify_order(  # noqa: C901
        self,
        exchange: str,
        order_id: str,
        order_type: str,
        price: float,
        price_type: str,
        product_type: str,
        quantity: int,
        tradingsymbol: str,
        amo: Union[str, None] = None,
        book_loss_price: Union[float, None] = None,
        book_profit_price: Union[float, None] = None,
        disclosed_quantity: Union[int, None] = None,
        market_protection: Union[float, None] = None,
        remarks: Union[str, None] = None,
        trailing_price: Union[float, None] = None,
        trigger_price: Union[float, None] = None,
        validity: str = "DAY",
    ) -> dict[str, Any]:
        """
        Modify an open order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_id`: Order ID of the order to be modified.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `price`: Price at which order is to be placed. Should be 0 for MARKET order.
        :param `price_type`: Price type. Valid values are MARKET, LIMIT, SL-MARKET, SL-LIMIT.
        :param `product_type`: Product type. Valid values are CNC, INTRADAY, NORMAL.
        :param `quantity`: Quantity to transact.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `amo`: If set to True, AMO order will be placed. Defaults to False.
        :param `book_loss_price`: Book loss price (Applicable only for Bracket orders).
        :param `book_profit_price`: Book profit price (Applicable only for Bracket orders).
        :param `disclosed_quantity`: Disclosed quantity for the order (Only for Equity and MCX).
        :param `market_protection`: Market protection percentage for the order (only for BSE and MCX).
        :param `remarks`: Remarks for the order.
        :param `trailing_price`: Trailing price for the order (Applicable only High Leverage product and Bracket order).
        :param `trigger_price`: Trigger price for the order (Applicable only for price_type, SL-MARKET or SL-LIMIT).
        :param `validity`: Validity for the order. Valid values are DAY, IOC, EOS. Defaults to DAY.
        :type `exchange`: `str`
        :type `order_id`: `str`
        :type `order_type`: `str`
        :type `price`: `float`
        :type `price_type`: `str`
        :type `product_type`: `str`
        :type `quantity`: `int`
        :type `tradingsymbol`: `str`
        :type `amo`: `str`
        :type `book_loss_price`: `float`
        :type `book_profit_price`: `float`
        :type `disclosed_quantity`: `int`
        :type `market_protection`: `float`
        :type `remarks`: `str`
        :type `trailing_price`: `float`
        :type `trigger_price`: `float`
        :type `validity`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if price_type not in self.c2i.price_types:
            raise ValueError("Invalid price type")

        if product_type not in self.c2i.product_types:
            raise ValueError("Invalid product type")

        if price_type == "MARKET" and price != 0:
            raise ValueError("Price should be 0 for market order")

        if price_type == "SL-LIMIT":
            if order_type == "BUY" and trigger_price and trigger_price > price:
                raise ValueError(
                    "Trigger price cannot be greater than price for SL-LIMIT BUY order"
                )
            elif (
                order_type == "SELL"
                and trigger_price
                and trigger_price < price
            ):
                raise ValueError(
                    "Trigger price cannot be lesser than price for SL-LIMIT SELL order"
                )

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="modify",
            method="POST",
            json_params=json_params,
        )

    def cancel_order(self, order_id: str) -> dict[str, Any]:
        """
        Cancel an order.

        :param `order_id`: Order ID of the order to be cancelled.
        :type `order_id`: `str`
        :return: Cancellation response details
        :rtype: `dict[str, Any]`
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="cancel/{order_id}",
            method="GET",
            url_params={"order_id": order_id},
        )

    def slice_order(  # noqa: C901
        self,
        exchange: str,
        order_type: str,
        price: float,
        price_type: str,
        product_type: str,
        quantity: int,
        slices: int,
        tradingsymbol: str,
        amo: Union[str, None] = None,
        book_loss_price: Union[float, None] = None,
        book_profit_price: Union[float, None] = None,
        disclosed_quantity: Union[int, None] = None,
        market_protection: Union[float, None] = None,
        remarks: Union[str, None] = None,
        trailing_price: Union[float, None] = None,
        trigger_price: Union[float, None] = None,
        validity: str = "DAY",
    ) -> dict[str, Any]:
        """
        Slice an order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `price`: Price at which order is to be placed. Should be 0 for MARKET order.
        :param `price_type`: Price type. Valid values are MARKET, LIMIT, SL-MARKET, SL-LIMIT.
        :param `product_type`: Product type. Valid values are CNC, INTRADAY, NORMAL.
        :param `quantity`: Quantity to transact.
        :param `slices`: Number of slices.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `amo`: If set to True, AMO order will be placed. Defaults to False.
        :param `book_loss_price`: Book loss price (Applicable only for Bracket orders).
        :param `book_profit_price`: Book profit price (Applicable only for Bracket orders).
        :param `disclosed_quantity`: Disclosed quantity for the order (Only for Equity and MCX).
        :param `market_protection`: Market protection percentage for the order (only for BSE and MCX).
        :param `remarks`: Remarks for the order.
        :param `trailing_price`: Trailing price for the order (Applicable only High Leverage product and Bracket order).
        :param `trigger_price`: Trigger price for the order (Applicable only for price_type, SL-MARKET or SL-LIMIT).
        :param `validity`: Validity for the order. Valid values are DAY, IOC, EOS. Defaults to DAY.
        :type `exchange`: `str`
        :type `order_id`: `str`
        :type `order_type`: `str`
        :type `price`: `float`
        :type `price_type`: `str`
        :type `product_type`: `str`
        :type `quantity`: `int`
        :type `slices`: `int`
        :type `tradingsymbol`: `str`
        :type `amo`: `str`
        :type `book_loss_price`: `float`
        :type `book_profit_price`: `float`
        :type `disclosed_quantity`: `int`
        :type `market_protection`: `float`
        :type `remarks`: `str`
        :type `trailing_price`: `float`
        :type `trigger_price`: `float`
        :type `validity`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if price_type not in self.c2i.price_types:
            raise ValueError("Invalid price type")

        if product_type not in self.c2i.product_types:
            raise ValueError("Invalid product type")

        if price_type == "MARKET" and price != 0:
            raise ValueError("Price should be 0 for market order")

        if price_type == "SL-LIMIT":
            if order_type == "BUY" and trigger_price and trigger_price > price:
                raise ValueError(
                    "Trigger price cannot be greater than price for SL-LIMIT BUY order"
                )
            elif (
                order_type == "SELL"
                and trigger_price
                and trigger_price < price
            ):
                raise ValueError(
                    "Trigger price cannot be lesser than price for SL-LIMIT SELL order"
                )

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="sliceorder",
            method="POST",
            json_params=json_params,
        )

    def convert_position_product_type(
        self,
        exchange: str,
        order_type: str,
        previous_product: str,
        product_type: str,
        quantity: int,
        tradingsymbol: str,
        position_type: str = "DAY",
    ) -> dict[str, Any]:
        """
        Convert an open position's product type.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `previous_product`: Previous product type. Valid values are CNC, INTRADAY, NORMAL.
        :param `product_type`: Product type. Valid values are CNC, INTRADAY, NORMAL.
        :param `quantity`: Quantity to transact.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `position_type`: Position type. Valid values are DAY, IOC, EOS.
        :type `exchange`: `str`
        :type `order_id`: `str`
        :type `order_type`: `str`
        :type `previous_product`: `str`
        :type `product_type`: `str`
        :type `quantity`: `int`
        :type `tradingsymbol`: `str`
        :type `position_type`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if (
            product_type not in self.c2i.product_types
            or previous_product not in self.c2i.product_types
        ):
            raise ValueError("Invalid product type")

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="productconversion",
            method="POST",
            json_params=json_params,
        )

    def place_gtt_order(
        self,
        exchange: str,
        order_type: str,
        price: float,
        quantity: int,
        tradingsymbol: str,
        alert_price: float,
        condition: str,
    ) -> dict[str, Any]:
        """
        Place a GTT order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `price`: Price at which order is to be placed.
        :param `quantity`: Quantity to transact.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `alert_price`: Price at which alert is to be triggered.
        :param `condition`: Condition to be met. Valid values are LTP_BELOW, LTP_ABOVE.
        :type `exchange`: `str`
        :type `order_type`: `str`
        :type `price`: `float`
        :type `product_type`: `str`
        :type `quantity`: `int`
        :type `tradingsymbol`: `str`
        :type `alert_price`: `float`
        :type `condition`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        if condition not in self.c2i.gtt_condition_types:
            raise ValueError("Invalid GTT condition")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="gttplaceorder",
            method="POST",
            json_params=json_params,
        )

    def modify_gtt_order(
        self,
        exchange: str,
        alert_id: str,
        order_type: str,
        price: float,
        quantity: int,
        tradingsymbol: str,
        alert_price: float,
        condition: str,
    ) -> dict[str, Any]:
        """
        Modify a GTT order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `alert_id`: Alert id of the GTT order.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `price`: Price at which order is to be placed.
        :param `quantity`: Quantity to transact.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `alert_price`: Price at which alert is to be triggered.
        :param `condition`: Condition to be met. Valid values are LTP_BELOW, LTP_ABOVE.
        :type `exchange`: `str`
        :type `alert_id`: `str`
        :type `order_type`: `str`
        :type `price`: `float`
        :type `quantity`: `int`
        :type `tradingsymbol`: `str`
        :type `alert_price`: `float`
        :type `condition`: `str`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if quantity == 0:
            raise ValueError("Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="gttmodify",
            method="POST",
            json_params=json_params,
        )

    def cancel_gtt_order(self, alert_id: str) -> dict[str, Any]:
        """
        Cancel a GTT order.

        :param `alert_id`: Alert id of the GTT order.
        :type `alert_id`: `str`
        :return: Cancellation response details
        :rtype: `dict[str, Any]`
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="gttcancel/{alert_id}",
            method="GET",
            url_params={"alert_id": alert_id},
        )

    def place_oco_order(
        self,
        exchange: str,
        order_type: str,
        tradingsymbol: str,
        stoploss_quantity: int,
        stoploss_price: float,
        target_quantity: int,
        target_price: float,
        remarks: Union[str, None] = None,
    ) -> dict[str, Any]:
        """
        Place an OCO order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `stoploss_quantity`: Quantity of stoploss order.
        :param `stoploss_price`: Price of stoploss order.
        :param `target_quantity`: Quantity of target order.
        :param `target_price`: Price of target order.
        :param `remarks`: Remarks if any.
        :type `exchange`: `str`
        :type `order_type`: `str`
        :type `tradingsymbol`: `str`
        :type `stoploss_quantity`: `int`
        :type `stoploss_price`: `float`
        :type `target_quantity`: `int`
        :type `target_price`: `float`
        :type `remarks`: `Union[str, None]`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if stoploss_quantity == 0:
            raise ValueError("Stoploss Quantity cannot be 0")

        if target_quantity == 0:
            raise ValueError("Target Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="ocoplaceorder",
            method="POST",
            json_params=json_params,
        )

    def modify_oco_order(
        self,
        exchange: str,
        alert_id: str,
        order_type: str,
        tradingsymbol: str,
        stoploss_quantity: int,
        stoploss_price: float,
        target_quantity: int,
        target_price: float,
        remarks: Union[str, None] = None,
    ) -> dict[str, Any]:
        """
        Modify an OCO order.

        :param `exchange`: Exchange in which security is listed. Currently NSE, BSE, NFO, CDS, MCX are supported.
        :param `alert_id`: Alert id of the OCO order.
        :param `order_type`: Order type. Valid values are BUY, SELL.
        :param `tradingsymbol`: Trading symbol of security to transact.
        :param `stoploss_quantity`: Quantity of stoploss order.
        :param `stoploss_price`: Price of stoploss order.
        :param `target_quantity`: Quantity of target order.
        :param `target_price`: Price of target order.
        :param `remarks`: Remarks if any.
        :type `exchange`: `str`
        :type `alert_id`: `str`
        :type `order_type`: `str`
        :type `tradingsymbol`: `str`
        :type `stoploss_quantity`: `int`
        :type `stoploss_price`: `float`
        :type `target_quantity`: `int`
        :type `target_price`: `float`
        :type `remarks`: `Union[str, None]`
        :return: The order details
        :rtype: `dict[str, Any]`
        """
        if exchange not in self.c2i.exchange_types:
            raise ValueError("Invalid exchange type")

        if order_type not in self.c2i.order_types:
            raise ValueError("Invalid order type")

        if stoploss_quantity == 0:
            raise ValueError("Stoploss Quantity cannot be 0")

        if target_quantity == 0:
            raise ValueError("Target Quantity cannot be 0")

        json_params: dict[str, Any] = locals()
        for k in list(json_params.keys()):
            if k == "self" or json_params[k] is None:
                del json_params[k]

        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="ocomodify",
            method="POST",
            json_params=json_params,
        )

    def cancel_oco_order(self, alert_id: str) -> dict[str, Any]:
        """
        Cancel a OCO order.

        :param `alert_id`: Alert id of the OCO order.
        :type `alert_id`: `str`
        :return: Cancellation response details
        :rtype: `dict[str, Any]`
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="ococancel/{alert_id}",
            method="GET",
            url_params={"alert_id": alert_id},
        )

    def orders(self) -> dict[str, Any]:
        """
        Get list of orders.

        :return: List of orders.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="orders",
            method="GET",
        )

    def order(self, order_id: str) -> dict[str, Any]:
        """
        Get status of a order.

        :return: Order status.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="order/{order_id}",
            method="GET",
            url_params={"order_id": order_id},
        )

    def gtt_orders(self) -> dict[str, Any]:
        """
        Get list of GTT orders.

        :return: List of GTT orders.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="gttorders",
            method="GET",
        )

    def trades(self) -> dict[str, Any]:
        """
        Retrieve the list of trades executed.

        :return: List of trades executed.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="trades",
            method="GET",
        )

    def positions(self) -> dict[str, Any]:
        """
        Retrieve the list of positions.

        :return: List of positions.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="positions",
            method="GET",
        )

    def holdings(self) -> dict[str, Any]:
        """
        Retrieve the list of holdings.

        :return: List of holdings.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="holdings",
            method="GET",
        )

    def limits(self) -> dict[str, Any]:
        """
        Get account balance and cash margin details for all segments.

        :return: Account balance and cash margin details for all segments.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="limits",
            method="GET",
        )

    def margins(self, orders: list[dict[str, Any]]) -> dict[str, Any]:
        """
        Get margin for a list of orders.

        :param orders: List of orders.
        :type orders: list[dict[str, str]]
        :return: Margin for a list of orders.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="margin",
            method="POST",
            json_params={"basketlists": orders},
        )

    def span_calculator(
        self, positions: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """
        Get span information for a list of positions.

        :param positions: List of positions.
        :type positions: list[dict[str, str]]
        :return: Span information for a list of positions.
        :rtype: dict[str, Any]
        """
        return self.c2i.send_request(
            route_prefix=self.c2i.base_url,
            route="spancalculator",
            method="POST",
            json_params={"positions": positions},
        )
