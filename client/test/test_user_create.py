# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import chat_rpg_client
from chat_rpg_client.models.user_create import UserCreate  # noqa: E501
from chat_rpg_client.rest import ApiException

class TestUserCreate(unittest.TestCase):
    """UserCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreate`
        """
        model = chat_rpg_client.models.user_create.UserCreate()  # noqa: E501
        if include_optional :
            return UserCreate(
                username = None, 
                name = None, 
                email = None, 
                password = None, 
                avatar = None
            )
        else :
            return UserCreate(
                username = None,
                name = None,
                email = None,
                password = None,
        )
        """

    def testUserCreate(self):
        """Test UserCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
