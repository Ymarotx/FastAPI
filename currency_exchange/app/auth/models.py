from datetime import datetime
from typing import List, Optional,Generic
from fastapi_users.models import ID, OAP, UP

from sqlalchemy import Table, Integer, Column, String, JSON, TIMESTAMP, ForeignKey, Boolean
from database import metadata,Base
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseOAuthAccountTable,
    SQLAlchemyBaseUserTable,
    SQLAlchemyBaseUserTableUUID
)
from sqlalchemy.orm import Mapped, relationship

role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True,nullable=False),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
    extend_existing=True

)

class OAuthAccount(SQLAlchemyBaseOAuthAccountTable[int],Base):
    __tablename__ = "oauth_account"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True,nullable=False)
    oauth_name = Column(String(length=100), index=True, nullable=False)
    access_token = Column(String(length=1024), nullable=False)
    expires_at = Column(Integer, nullable=True)
    refresh_token = Column(String(length=1024), nullable=True)
    account_id = Column(String(length=320), index=True, nullable=False)
    account_email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="cascade"))



class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined",
    )


