from pydantic import BaseModel, Field
from typing import List, Union


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


class User(BaseModel):
    id: int
    role: str
    name: str


class UserResponse(BaseModel):
    status: int
    data: Union[List[User], str]
