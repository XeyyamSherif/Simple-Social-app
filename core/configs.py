from pydantic import BaseModel


class Config:
    DATABASE_URL = f'sqlite:///./test.db'


Configs = Config()


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
