from pydantic import BaseModel, Field, validator
from email_validator import validate_email, EmailNotValidError

from app.utils import check_mail


class SignUp(BaseModel):
    first_name: str = Field(..., description="first_name")
    mail: str = Field(..., description="mail")
    password: str = Field(..., description="password")

    @validator('mail')
    def country_phone(cls, v):
        if check_mail(v):
            return v
        else:
            raise ValueError('mail is invalid')