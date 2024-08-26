from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import User, SecretModel, CompanyModel, InviteModel


class AccountModel(BaseModel):
    __tablename__ = "account_table"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(EmailType, nullable=False, unique=True)
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"), nullable=True
    )
    user: Mapped["User"] = relationship(back_populates="account", lazy="selectin")
    secret: Mapped["SecretModel"] = relationship(
        back_populates="account", cascade="all, delete", passive_deletes=True
    )
    company: Mapped["CompanyModel"] = relationship(
        back_populates="director", passive_deletes=True
    )
    invite: Mapped["InviteModel"] = relationship(
        back_populates="account", cascade="all, delete", passive_deletes=True
    )
    __table_args__ = (UniqueConstraint("user_id"),)
