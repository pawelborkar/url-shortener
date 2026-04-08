from datetime import datetime
from sqlalchemy import DateTime, Boolean, String, func, text
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class USER(Base):
    __tablename__ = "user"

    """ Note: Any fields with has explicit data type and does not contain | None (Optionaal None) is by default have nullable=False set by SQLAlchemy under the hood."""
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(datetime.UTC), server_default=func.now()
    )
    update_at: Mapped[datetime | None] = mapped_column(
        DateTime(datetime.UTC), on_update=func.now(), nullable=True
    )
