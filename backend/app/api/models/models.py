from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    password: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone_number: int = Field(gt=7, lt=20)
