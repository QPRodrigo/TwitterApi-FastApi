# Python
from uuid import UUID
from datetime import date
from typing import Optional

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
        min_length=8
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
    pass

# Path Operator.
@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}
