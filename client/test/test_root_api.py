# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import chat_rpg_client
from chat_rpg_client.api.root_api import RootApi  # noqa: E501
from chat_rpg_client.rest import ApiException


class TestRootApi(unittest.TestCase):
    """RootApi unit test stubs"""

    def setUp(self):
        self.api = chat_rpg_client.api.root_api.RootApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_root_get(self):
        """Test case for root_get

        Read Root  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
