"""
User models
"""

# # System # #

# # Packages # #
from beanie import Document, PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from pymongo import IndexModel, ASCENDING

# # Project # #

###


class UserDoc(Document):
    """
    User database document
    """

    class Settings:
        collection = "users"
        indexes = [
            IndexModel([("username", ASCENDING)], unique=True),
            IndexModel([("email", ASCENDING)], unique=True),
            IndexModel([("name", ASCENDING)], unique=False),
        ]

    username: str = Field(..., max_length=50)
    name: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    avatar: str | None = None
    is_admin: bool = Field(False)

    @classmethod
    async def create(
        cls,
        username: str,
        name: str,
        email: str,
        password: str,
        avatar: str | None = None,
        is_admin: bool = False,
    ) -> "UserDoc":
        """
        Creates a new user with the given username, email and password.
        """
        user_doc = cls(
            username=username,
            name=name,
            email=email,
            password=password,
            avatar=avatar,
            is_admin=is_admin,
        )
        await user_doc.insert()
        return user_doc


class UserCreate(BaseModel):
    """
    New user data
    """

    username: str
    name: str
    email: EmailStr
    password: str
    avatar: str | None = None


class UserUpdate(BaseModel):
    """
    Update of user data
    """

    username: str | None = None
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    avatar: str | None = None
    is_admin: bool | None = None


class User(BaseModel):
    """
    Output of user data
    """

    id: PydanticObjectId = Field(..., alias="_id")
    username: str
    name: str
    email: EmailStr
    password: str
    avatar: str | None = None
    is_admin: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PydanticObjectId: str}
