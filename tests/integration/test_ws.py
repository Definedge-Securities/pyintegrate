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


from integrate import IntegrateWebSocket


# Callback called when the WebSocket connection is established and the login is successful.
def on_login(iws: IntegrateWebSocket) -> None:
    # Subscribe to a list of symbols (TCS and TATAMOTORS here).
    assert True
    iws.close(1000, "Closing connection")


# Callback to receive acknowledgements of the requests sent.
def on_acknowledgement(iws: IntegrateWebSocket, ack: dict[str, str]) -> None:
    assert True


def on_close(iws: IntegrateWebSocket, code: int, reason: str) -> None:
    iws.stop()


def test_websocket(iwebsocket: IntegrateWebSocket) -> None:
    # Assign the callbacks to the IntegrateWebSocket object.
    iwebsocket.on_login = on_login  # type: ignore
    iwebsocket.on_acknowledgement = on_acknowledgement  # type: ignore
    iwebsocket.on_close = on_close  # type: ignore

    # Blocking WebSocket connection below.
    iwebsocket.connect()
    assert True
