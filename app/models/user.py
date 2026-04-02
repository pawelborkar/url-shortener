import timezone
from sqlalchemy.orm DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass


class USER(Base):

    __tablename__ = 'user'

    id: int | None
    username: str = mapped_column(String(16), unique=True)
    email: str = mapped_column(unique=True)
    password: str = mapped_column()
    is_active: int = mapped_column(1)

    created_at: DateTime = mapped_column(DateTime(timezone.utc), server_default=func.now())
    update_at: DateTime = mapped_column(DateTime(timezone.utc), server_default=func.now())
