from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.posts.models.post import Posts
from core.exceptions import NotFoundException
from core.exceptions.user import PostNotFoundException


class PostRepo:

    def add_post(self, data: dict, db: Session):
        post = Posts(**data)
        db.add(post)
        db.commit()
        return post

    def delete_post(self, _id: int, db: Session):
        try:
            post = db.query(Posts).filter(Posts.id == _id).first()
            db.delete(post)
            db.commit()
            return True
        except SQLAlchemyError:
            raise PostNotFoundException

    def read_all_posts(self, db: Session):
        posts = db.query(Posts).all()
        return posts

    def update_post(self, id: int, updated_data: dict, db: Session):
        post = db.query(Posts).filter(Posts.id == id).first()
        if post is not None:
            for key, value in updated_data.items():
                setattr(post, key, value)
            db.add(post)
            db.commit()
            db.refresh(post)
            return post
        else:
            raise PostNotFoundException

    def get_post_by_id(self, _id, db):
        try:
            post = db.query(Posts).filter(Posts.id == _id).first()
            return post
        except SQLAlchemyError:
            raise PostNotFoundException
