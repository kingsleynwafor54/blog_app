from pydantic import BaseModel 
from typing import List
import datetime as dt

class _PostBase(BaseModel):
    title:str
    content:str


class PostCreate(_PostBase):
    pass


class  Post(_PostBase):
    id:int
    owner_id=int
    date_created= dt.datetime

    class Config:
        orm_mode=True

class  _UserCreate(BaseModel):
    password: str

class User(_UserBase):
    id:int
    is_active: bool
    posts:List[Post]=[]

    class Config:
        orm_mode=True
