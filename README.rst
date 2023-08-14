Definedge Securities Integrate Python API Client
================================================

Introduction
------------
This is the official Python API client for the Definege Securities Integrate API platform.

The Definedge Securities API platform `Integrate <https://www.definedgesecurities.com/api-documentation/>`__ allows you to build trading and investment services platforms, execute strategies, and much more. You can execute & modify orders in real time in equities, derivatives, currencies and commodities. You can also manage user portfolios, access live market data and much more with a lightning fast API.

We offer resource-based URLs that accept JSON or form-encoded requests. The response is returned as JSON-encoded responses using Standard HTTP response codes, verbs, after authentication.

Installation
------------
Install the Definedge Securities Integrate Python API client. For more information, see the `Python API client documentation <https://pyintegrate.readthedocs.io/en/latest/>`__.

- Using pip:

.. code:: console

        pip install pyintegrate

- or Using poetry:

.. code:: console

        poetry add pyintegrate

Usage
-----
Order placement
...............
Simple example to place an order and get the order book:

.. code:: python

    from logging import INFO, basicConfig, info
    from typing import Any

    from integrate import ConnectToIntegrate, IntegrateOrders

    basicConfig(level=INFO)

    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )

    io = IntegrateOrders(conn)

    try:
        order: dict[str, Any] = io.place_order(
            exchange=conn.EXCHANGE_TYPE_NSE,
            order_type=conn.ORDER_TYPE_BUY,
            price=0,
            price_type=conn.PRICE_TYPE_MARKET,
            product_type=conn.PRODUCT_TYPE_INTRADAY,
            quantity=1,
            tradingsymbol="SBIN-EQ",
        )
        info(f"Order placed: {order}")
    except Exception as e:
        info(f"Order placement failed: {e}")

    # Get order book.
    info(io.orders())


WebSocket streaming
...................
Simple example to stream live quotes, get order and depth updates:

.. code:: python

    from logging import INFO, basicConfig, info

    from integrate import ConnectToIntegrate, IntegrateWebSocket

    basicConfig(level=INFO)


    # Callback called when the WebSocket connection is established and the login is successful.
    def on_login(iws: IntegrateWebSocket) -> None:
        # Subscribe to a list of symbols (TCS and TATAMOTORS here).
        tokens: list[tuple[str, str]] = [
            (iws.c2i.EXCHANGE_TYPE_NSE, "11536"),
            (iws.c2i.EXCHANGE_TYPE_NSE, "3456"),
        ]
        # Subscribe to a list of symbols. You can have different lists for different subscriptions.
        iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_TICK, tokens)
        iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_ORDER, tokens)
        iws.subscribe(iws.c2i.SUBSCRIPTION_TYPE_DEPTH, tokens)


    # Callback to receive ticks.
    def on_tick_update(iws: IntegrateWebSocket, tick: dict[str, str]) -> None:
        # Callback to receive ticks.
        info(f"Ticks: {tick}")


    # Callback to receive order updates.
    def on_order_update(iws: IntegrateWebSocket, order: dict[str, str]) -> None:
        info(f"Order update : {order}")


    # Callback to receive bid-ask depth updates.
    def on_depth_update(iws: IntegrateWebSocket, depth: dict[str, str]) -> None:
        info(f"Depth update : {depth}")


    # Callback to receive acknowledgements of the requests sent.
    def on_acknowledgement(iws: IntegrateWebSocket, ack: dict[str, str]) -> None:
        info(f"Ack : {ack}")


    # Callback to receive Python exceptions.
    def on_exception(iws: IntegrateWebSocket, e: Exception) -> None:
        info(f"Exception : {e}")
        # Below will close the WebSocket connection.
        # iws.close_on_exception("Closing connection due to exception")


    # Callback to run on WebSocket close.
    def on_close(iws: IntegrateWebSocket, code: int, reason: str) -> None:
        info(f"Closed : {code} {reason}")
        # Below will stop the event loop and the program will exit.
        # iws.stop()


    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )
    iws = IntegrateWebSocket(conn)

    # Assign the callbacks.
    iws.on_login = on_login
    iws.on_tick_update = on_tick_update
    iws.on_order_update = on_order_update
    iws.on_depth_update = on_depth_update
    iws.on_acknowledgement = on_acknowledgement
    iws.on_exception = on_exception
    iws.on_close = on_close

    # Blocking WebSocket connection below. Nothing after this will run.
    # You have to use the callbacks for further management.
    # If you receive an SSL Error after login, then replace the below line with:
    # iws.connect(ssl_verify=False)
    iws.connect()

Check out more examples in the examples_ folder.

.. _examples: https://github.com/Definedge-Securities/pyintegrate/tree/main/examples

Contributing_
-------------
.. _Contributing: https://github.com/Definedge-Securities/pyintegrate/tree/main/CONTRIBUTING.md
