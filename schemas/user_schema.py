from pydantic import BaseModel

# from datetime import datetime


class UserDto(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserUpdate(BaseModel):
    id: int
    name: str | None = None
    email: str | None = None
    password: str | None = None

    class Config:
        extra = "forbid"
