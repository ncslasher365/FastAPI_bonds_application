from datetime import datetime

from pydantic import BaseModel


class OperationBase(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    operation_type: str

    class Config:
        orm_mode = True
