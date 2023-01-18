from pydantic import BaseModel, Field, validator


class CreatePost(BaseModel):
    content: str = Field(..., description="content")
    title: str = Field(..., description="title")



