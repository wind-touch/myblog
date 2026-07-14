from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str