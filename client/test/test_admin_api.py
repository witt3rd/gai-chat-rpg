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
from chat_rpg_client.api.admin_api import AdminApi  # noqa: E501
from chat_rpg_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = chat_rpg_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_db_admin_db_delete(self):
        """Test case for db_admin_db_delete

        Drop Db  # noqa: E501
        """
        pass

    def test_db_admin_db_delete_0(self):
        """Test case for db_admin_db_delete_0

        Drop Db  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
