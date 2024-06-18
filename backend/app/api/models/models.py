from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    password: str = Field(min_length=3, max_length=20)
    firstname: str = Field(min_length=1, max_length=20)
    lastname: str = Field(min_length=1, max_length=20)
    email: EmailStr
    phone_number: str = Field(min_length=7, max_length=20)


class Card(BaseModel):
    type: str = Field(min_length=5, max_length=6, examples=["credit", "debit"])
    design: str = Field(min_length=4)


