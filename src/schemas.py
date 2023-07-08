from typing import Optional
from datetime import datetime, date

from pydantic import BaseModel, EmailStr, Field


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr
    phone_number: str = Field(max_length=20)
    birthday: date = Field(description="Date format 'YYYY-MM-DD'")
    additional_data: Optional[str] = Field(max_length=20)


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_data: str = 'Additional data (Optional)'
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserDb(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
