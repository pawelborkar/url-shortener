import timezone
from sqlalchemy import String, DateTime, Number
from sqlalchemy.orm import DeclarativeBase, mapped_column, func

class Base(DeclarativeBase):
    pass

class URL(Base):

    __tablename__ = 'urls'
    
    id: int | None = mapped_column(primary_key=True)
    short_code: str = mapped_column(String(8), unique=True)
    url: str = mapped_column(String(32000))  # Explicitly setting arbitary value for the destination URL in order to avoid pollution
    # user: int: USER.id
    count: int = mapped_column(Number(1))
    created_at: DateTime = mapped_column(DateTime(timezone.utc), server_default=func.now())
    expires_at: DateTime = mapped_column(DateTime(timezone.utc), server_default=func.now())
    updated_at: DateTime = mapped_column(DateTime(timezone.utc), server_default=func.now())
