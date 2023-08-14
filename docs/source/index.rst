Definedge Securities Integrate Python API Client
================================================

Introduction
------------
This is the official Python API client for the Definege Securities Integrate API platform.

The Definedge Securities API platform `Integrate <https://www.definedgesecurities.com/api-documentation/>`__ allows you to build trading and investment services platforms, execute strategies, and much more.

You can execute & modify orders in real time in equities, derivatives, currencies and commodities. You can also manage user portfolios, access live market data and much more with a lightning fast API.

We offer resource-based URLs that accept JSON or form-encoded requests. The response is returned as JSON-encoded responses using Standard HTTP response codes, verbs, after authentication.

Installation
------------
Install the Definedge Securities Integrate Python API client

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

.. include:: ../../examples/orders.py
    :literal:

WebSocket streaming
...................
Simple example to stream live quotes, get order and depth updates:

.. include:: ../../examples/ws.py
    :literal:

Check out more examples under `Examples <examples.html>`__.

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

.. note:: Integration tests require a valid API secret as the orders would be placed on the live market. Please use a test account for integration testing.

.. toctree::
    :maxdepth: 2
    :hidden:

    examples
    integrate
