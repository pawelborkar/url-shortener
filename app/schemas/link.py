from datetime import datetime
from pydantic import BaseModel, HttpUrl, ConfigDict
import logfire

logfire.configure()
logfire.instrument_pydantic()


class LinkBase(BaseModel):
    url: HttpUrl


class LinkRequest(LinkBase):
    pass


class LinkPublicResponse(LinkBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    short_code: str
    url: HttpUrl
    created_at: datetime


class LinkResponse(LinkPublicResponse):
    model_config = ConfigDict(from_attributes=True)
    count: int
    updated_at: datetime | None = None


class LinkAdminResponse(LinkResponse):
    model_config = ConfigDict(
        from_attributes=True
    )  # Although it will inherit from LinkResponse class but still adding it to be explicit and consistency.
    user_id: int | None = None
