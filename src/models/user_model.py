from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING
from src.schemas.user_schema import UserDB

if TYPE_CHECKING:
    from src.models import (
        SecretModel,
        AccountModel,
        MemberModel,
        UserPositionModel,
        TaskModel,
    )



class User(BaseModel):
    __tablename__ = "user_table"

    id: Mapped[uuid_pk]
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    registered_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    account: Mapped["AccountModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    secret: Mapped["SecretModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True, lazy="selectin"
    )
    member: Mapped["MemberModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True, lazy="selectin"
    )
    user_position: Mapped["UserPositionModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True
    )
    author: Mapped["TaskModel"] = relationship(
        back_populates="author_user",
        passive_deletes=True,
        foreign_keys="TaskModel.author_id",
    )
    responsible: Mapped["TaskModel"] = relationship(
        back_populates="responsible_user",
        passive_deletes=True,
        foreign_keys="TaskModel.responsible_id",
    )

    def to_pydantic_schema(self) -> UserDB:
        return UserDB(**self.__dict__)




#
# 3beeb1f1-2ec2-475e-bd38-4952f2e4235b
# 2831e77b-463d-4678-b261-cb52684db28a
# f12fa086-3655-425a-8c82-86d7c815c021
# 110695f4-292c-4bff-98de-c45d39994726
# cce70000-91d0-4f51-81a1-a7b18877b5f3