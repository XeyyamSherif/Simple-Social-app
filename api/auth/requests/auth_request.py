from pydantic import BaseModel, Field, validator


class LogIn(BaseModel):
    mail: str = Field(..., description="mail")
    password: str = Field(..., description="password")