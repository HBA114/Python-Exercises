from typing import List
from pydantic import BaseModel
from datetime import datetime


class _PostBase(BaseModel):
    title: str
    photo_base64: str

    class Config:
        orm_mode = True


class PostCreate(_PostBase):
    pass  # will work from _PostBase


class Post(_PostBase):
    id: int
    owner_id: int
    date_created: datetime


class _UserBase(BaseModel):
    email: str
    photo_base64: str

    class Config:
        orm_mode = True


class UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []