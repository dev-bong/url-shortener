from pydantic import BaseModel, Field


class ShortenerInput(BaseModel):
    url: str = Field(default=..., description="원본 URL")
    duration: int | None = Field(default=None, description="단축 URL 지속일수")


class ShortURL(BaseModel):
    short_url: str = Field(default=..., description="단축 URL")
