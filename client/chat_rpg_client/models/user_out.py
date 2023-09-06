# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field

class UserOut(BaseModel):
    """
    Output of user data
    """
    username: Optional[Any] = Field(...)
    name: Optional[Any] = Field(...)
    email: Optional[Any] = Field(...)
    password: Optional[Any] = Field(...)
    is_admin: Optional[Any] = Field(...)
    __properties = ["username", "name", "email", "password", "is_admin"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> UserOut:
        """Create an instance of UserOut from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if is_admin (nullable) is None
        # and __fields_set__ contains the field
        if self.is_admin is None and "is_admin" in self.__fields_set__:
            _dict['is_admin'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserOut:
        """Create an instance of UserOut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserOut.parse_obj(obj)

        _obj = UserOut.parse_obj({
            "username": obj.get("username"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "password": obj.get("password"),
            "is_admin": obj.get("is_admin")
        })
        return _obj


