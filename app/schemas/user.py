from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    profile_picture: str | None = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: UUID

    class Config:
        orm_mode = True