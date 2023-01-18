from sqlalchemy import Column, Integer, String
from app.base_class import Base


class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mail = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
