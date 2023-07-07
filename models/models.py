from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON
from datetime import datetime

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    permissions = Column(JSON)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    registered_at = Column(TIMESTAMP(), default=datetime.utcnow)
    role_id = Column(Integer(), ForeignKey('roles.id'))
