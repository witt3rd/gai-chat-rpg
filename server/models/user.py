"""
User models
"""

# # System # #

# # Packages # #
from beanie import Document
from pydantic import BaseModel, EmailStr, Field
from pymongo import IndexModel, ASCENDING

# # Project # #

###


class UserDoc(Document):
    class Settings:
        collection = "users"
        indexes = [
            IndexModel([("username", ASCENDING)], unique=True),
            IndexModel([("email", ASCENDING)], unique=True),
        ]

    username: str = Field(..., max_length=50)
    name: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    is_admin: bool = Field(False)

    @classmethod
    async def create(
        cls,
        username: str,
        name: str,
        email: str,
        password: str,
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
            is_admin=is_admin,
        )
        await user_doc.insert()
        return user_doc


class UserSignup(BaseModel):
    """
    Model to handle data of signup request
    """

    username: str
    name: str
    email: EmailStr
    password: str


class UserIn(BaseModel):
    """
    Update of user data
    """

    username: str | None = None
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    is_admin: bool | None = None


class UserOut(BaseModel):
    """
    Output of user data
    """

    id: str
    username: str
    name: str
    email: EmailStr
    password: str
    is_admin: bool
