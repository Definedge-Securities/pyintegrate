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
This module contains functions that help in testing.
"""

from json import loads
from os.path import abspath, dirname, join
from typing import Any


def get_mock_response(filename: str) -> str:
    """
    Get mock response based on route.

    :param filename: Filename of mock response.
    :type filename: str
    :return: Mock response.
    :rtype: str
    :raises FileNotFoundError: If mock response file is not found.
    """
    mock_response_path: str = "mock_responses"
    mock_response_file: str = abspath(
        join(dirname(__file__), mock_response_path, filename)
    )
    return open(mock_response_file, "r").read()


def compare_keys(filename: str, actual_response: dict[str, Any]) -> bool:
    """
    Compare keys of actual response with mock response recursively.

    :param filename: Filename of mock response.
    :type filename: str
    :param actual_response: Actual response.
    :type actual_response: dict[str, Any]
    :return: True if keys match, False otherwise.
    :rtype: bool
    """
    mock_response: dict[str, Any] = loads(get_mock_response(filename))
    for key in mock_response.keys():
        if key not in actual_response.keys():
            return False
        if isinstance(mock_response[key], dict):
            if not compare_keys(filename, actual_response[key]):
                return False
    return True
