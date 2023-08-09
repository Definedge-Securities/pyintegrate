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
    from typing import Union

    from integrate import ConnectToIntegrate, IntegrateWebSocket

    basicConfig(level=INFO)

    # Initialise the connection and login.
    conn = ConnectToIntegrate()
    conn.login(
        api_token="YOUR_API_TOKEN",
        api_secret="YOUR_API_SECRET",
    )


    # Callback called when the WebSocket connection is established and the login is successful.
    def on_login(iws: IntegrateWebSocket) -> None:
        # Subscribe to a list of symbols (TCS and TATAMOTORS here).
        tokens: list[tuple[str, str]] = [
            (iws.c2i.EXCHANGE_TYPE_NSE, "11536"),
            (iws.c2i.EXCHANGE_TYPE_NSE, "3456"),
        ]
        # Subscribe to a list of symbols. You can have different lists for different subscriptions.
        iws.subscribe(conn.SUBSCRIPTION_TYPE_TICK, tokens)
        iws.subscribe(conn.SUBSCRIPTION_TYPE_DEPTH, tokens)


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


    iws = IntegrateWebSocket(conn)

    # Assign the callbacks.
    iws.on_login = on_login
    iws.on_tick_update = on_tick_update
    iws.on_order_update = on_order_update
    iws.on_depth_update = on_depth_update
    iws.on_acknowledgement = on_acknowledgement

    # Blocking WebSocket connection below. Nothing after this will run.
    # You have to use the callbacks for further management.
    iws.connect()

Check out more examples in the examples_ folder.

.. _examples: https://github.com/Definedge-Securities/pyintegrate/tree/main/examples

Testing
-------
Clone the repository

.. code:: console

    git clone https://github.com/definedge/pyintegrate.git

Install the dependencies using poetry

.. code:: console

    poetry install

Run unit tests

.. code:: console

    poetry run pytest -s tests/unit

Run integration tests

.. code:: console

    poetry run pytest -s tests/integration --apiToken "api_token" --apiSecret "api_secret" --totp "totp"

OR you can store the session keys and use them for subsequent runs as below

.. code:: console

    poetry run pytest -s tests/integration --uid "user_id" --actid "account_id" --apiSessionKey "api_session_key" --wsSessionKey "ws_session_key"

Note
----
Integration tests require a valid API secret as the orders would be placed on the live market. Please use a test account for integration testing.
