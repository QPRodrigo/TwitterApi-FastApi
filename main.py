# Python
from uuid import UUID
from datetime import date
from typing import Optional
from datetime import datetime

# FastAPI
from fastapi import FastAPI

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

app = FastAPI()

# Models

##Model Users
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

## Model Tweet
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_length=1, 
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operator.
@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
