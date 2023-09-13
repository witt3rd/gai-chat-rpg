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

class Message(BaseModel):
    """
    Output of message data
    """
    id: Optional[Any] = Field(..., alias="_id")
    timestamp: Optional[Any] = Field(...)
    campaign: Optional[Any] = Field(...)
    sender: Optional[Any] = Field(...)
    target: Optional[Any] = Field(...)
    content: Optional[Any] = Field(...)
    is_edited: Optional[Any] = Field(...)
    __properties = ["_id", "timestamp", "campaign", "sender", "target", "content", "is_edited"]

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
    def from_json(cls, json_str: str) -> Message:
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['_id'] = None

        # set to None if timestamp (nullable) is None
        # and __fields_set__ contains the field
        if self.timestamp is None and "timestamp" in self.__fields_set__:
            _dict['timestamp'] = None

        # set to None if campaign (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign is None and "campaign" in self.__fields_set__:
            _dict['campaign'] = None

        # set to None if sender (nullable) is None
        # and __fields_set__ contains the field
        if self.sender is None and "sender" in self.__fields_set__:
            _dict['sender'] = None

        # set to None if target (nullable) is None
        # and __fields_set__ contains the field
        if self.target is None and "target" in self.__fields_set__:
            _dict['target'] = None

        # set to None if content (nullable) is None
        # and __fields_set__ contains the field
        if self.content is None and "content" in self.__fields_set__:
            _dict['content'] = None

        # set to None if is_edited (nullable) is None
        # and __fields_set__ contains the field
        if self.is_edited is None and "is_edited" in self.__fields_set__:
            _dict['is_edited'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Message:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Message.parse_obj(obj)

        _obj = Message.parse_obj({
            "id": obj.get("_id"),
            "timestamp": obj.get("timestamp"),
            "campaign": obj.get("campaign"),
            "sender": obj.get("sender"),
            "target": obj.get("target"),
            "content": obj.get("content"),
            "is_edited": obj.get("is_edited")
        })
        return _obj

