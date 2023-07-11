from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer(), primary_key=True)
    quantity = Column(String(255), nullable=False)
    figi = Column(String(255), nullable=False)
    instrument_type = Column(String(255), nullable=False)
    date = Column(TIMESTAMP(), default=datetime.utcnow)
    operation_type = Column(String(255), nullable=False)
