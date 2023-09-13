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
from chat_rpg_client.models.message import Message  # noqa: E501
from chat_rpg_client.rest import ApiException

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Message
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Message`
        """
        model = chat_rpg_client.models.message.Message()  # noqa: E501
        if include_optional :
            return Message(
                id = 5eb7cf5a86d9755df3a6c593, 
                timestamp = None, 
                campaign = 5eb7cf5a86d9755df3a6c593, 
                sender = 5eb7cf5a86d9755df3a6c593, 
                target = 5eb7cf5a86d9755df3a6c593, 
                content = None, 
                is_edited = None
            )
        else :
            return Message(
                id = 5eb7cf5a86d9755df3a6c593,
                timestamp = None,
                campaign = 5eb7cf5a86d9755df3a6c593,
                sender = 5eb7cf5a86d9755df3a6c593,
                target = 5eb7cf5a86d9755df3a6c593,
                content = None,
                is_edited = None,
        )
        """

    def testMessage(self):
        """Test Message"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()