from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, TIMESTAMP,\
    ForeignKey, Column, JSON, Boolean
from datetime import datetime

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    permissions = Column(JSON)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    username = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    registered_at = Column(TIMESTAMP(), default=datetime.utcnow)
    role_id = Column(Integer(), ForeignKey('role.id'))
    is_active = Column(Boolean(), default=True, nullable=False)
    is_superuser = Column(Boolean(), default=False, nullable=False)
    is_verified = Column(Boolean(), default=False, nullable=False)
