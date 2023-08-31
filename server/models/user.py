"""
User models
"""

# # System # #

# # Packages # #
from beanie import Document
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, Field
from pymongo import IndexModel, ASCENDING

# # Project # #

###

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserDoc(Document):
    class Settings:
        collection = "users"
        indexes = [
            IndexModel([("username", ASCENDING)], unique=True),
            IndexModel([("email", ASCENDING)], unique=True),
        ]

    username: str = Field(..., max_length=50)
    email: EmailStr
    hashed_password: str = Field(..., min_length=6)
    is_admin: bool = Field(False)

    def verify_password(self, password) -> bool:
        """
        Checks if the provided password matches the hashed password stored.
        """
        return pwd_context.verify(password, self.hashed_password)

    @classmethod
    async def create(
        cls, username: str, email: str, password: str, is_admin: bool = False
    ) -> "UserDoc":
        """
        Creates a new user with the given username, email and password.
        """
        hashed_password = pwd_context.hash(password)
        user_doc = cls(
            username=username,
            email=email,
            hashed_password=hashed_password,
            is_admin=is_admin,
        )
        await user_doc.insert()
        return user_doc


class UserSignup(BaseModel):
    """
    Model to handle data of signup request
    """

    username: str
    email: EmailStr
    password: str
