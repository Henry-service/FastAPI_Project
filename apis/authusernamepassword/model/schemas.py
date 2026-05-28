from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    username: str = Field(min_length=2, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8)


class UserRead(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr


class AuthRegisterResponse(BaseModel):
    success: Optional[str] = Field(alias="success", default=None)
    url: Optional[str] = Field(alias="url", default=None)


AuthRegisterResponse.model_rebuild()