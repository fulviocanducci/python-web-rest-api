from pydantic import BaseModel
from datetime import datetime


class CreditDto(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class CreditCreate(BaseModel):
    name: str


class CreditUpdate(BaseModel):
    id: int
    name: str | None = None
    created_at: datetime | None = None

    class Config:
        extra = "forbid"
