from datetime import datetime

from pydantic import BaseModel, Field


class ShortenerInput(BaseModel):
    url: str = Field(default=..., description="원본 URL")
    duration: int | None = Field(
        default=None, description="단축 URL 지속시간 (시간 단위)", ge=1
    )


class ShortURL(BaseModel):
    short_url: str = Field(default=..., description="단축 URL")


class URLstats(BaseModel):
    count: int = Field(default=..., description="단축 URL 조회수")
    latest: datetime = Field(default=..., description="단축 URL 최근 조회 시간")
