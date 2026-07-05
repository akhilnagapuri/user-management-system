from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    manager = "manager"
    user = "user"


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    mobile_number: str
    domain: str
    password: str
    role: UserRole


class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    mobile_number: str
    domain: str
    role: UserRole
    password: str | None = None


class UserListResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: UserRole
    is_deleted: bool


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    role: UserRole
    is_deleted: bool