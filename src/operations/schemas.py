from datetime import datetime

from pydantic import BaseModel, Field


class OperationBase(BaseModel):
    id: int
    quantity: str
    figi: str  # unique identifier
    instrument_type: str
    date: datetime = Field(example='2023-07-09 12:48:56.289215')
    operation_type: str

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass
