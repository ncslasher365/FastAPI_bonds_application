from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, TIMESTAMP,\
    ForeignKey, Column, JSON, Boolean
from datetime import datetime

from sqlalchemy.orm import mapped_column, Mapped, declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    permissions = Column(JSON)


class UserDB(Base):
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


class User(SQLAlchemyBaseUserTable[int], Base):
    __table_args__ = {'keep_existing': True}

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    email: Mapped[str] = mapped_column(
        String(length=255), unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(
        String(length=255), nullable=False, unique=True
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    registered_at = mapped_column(
        TIMESTAMP, default=datetime.utcnow
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("role.id")
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
