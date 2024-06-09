from pydantic import BaseModel, EmailStr
from typing import ClassVar

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True


class AttackDataSchemas(BaseModel):
    id: str
    name: str
    description: str
    timestamp: str
    some_class_var: ClassVar[str] = "some value"

    class Config:
        arbitrary_types_allowed = True
        # or if you need to ignore certain types
        # ignored_types = (SomeTypeToIgnore,)
