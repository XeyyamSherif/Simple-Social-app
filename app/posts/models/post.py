from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.base_class import Base


class Posts(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    like = Column(Integer, nullable=False, default=0)
    dislike = Column(Integer, nullable=False, default=0)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owners = relationship("Users", backref="posts")
