from datetime import datetime
from sqlalchemy import String, DateTime, func 
from sqlalchemy.orm import mapped_column, Mapped
from models.base import Base



class URL(Base):
    __tablename__ = "urls"

    id: Mapped[int] | None = mapped_column(primary_key=True)
    short_code: Mapped[str] = mapped_column(String(8), unique=True)
    url: Mapped[str] = mapped_column(
        String(32000)
    )  # Explicitly setting arbitary value for the destination URL in order to avoid pollution
    # user: Mapped[int]: USER.id
    count: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        DateTime(datetime.UTC), server_default=func.now()
    )
    # expires_at: Mapped[datetime] = mapped_column(
    #     DateTime(datetime.UTC.utc), server_default=func.now()
    # )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(datetime.UTC), server_default=func.now()
    )
