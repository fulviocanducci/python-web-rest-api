from pydantic import BaseModel


class LoginDto(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True
