from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.posts.repo.posts import PostRepo
from app.utils import object_as_dict
from core.schemas import BaseResponseSchema


class PostService:

    async def create_post(self, data: dict, db: Session):
        add_post = PostRepo().add_post(data, db)
        response = BaseResponseSchema(status=201, data=object_as_dict(add_post)).dict()
        return JSONResponse(status_code=201, content=response)

    async def delete_post(self, _id: int, db: Session):
        delete_post = PostRepo().delete_post(_id, db)
        if delete_post:
            response = BaseResponseSchema(status=200, message='deleted')
            return JSONResponse(status_code=200, content=response)

    async def read_all_posts(self, db: Session):
        all_posts = PostRepo().read_all_posts(db)
        response = BaseResponseSchema(status=200, data=[object_as_dict(post) for post in all_posts]).dict()
        return JSONResponse(status_code=200, content=response)

    async def update_post(self, _id: int, updated_data: dict, db: Session):
        update = PostRepo().update_post(_id, updated_data, db)
        response = BaseResponseSchema(status=200, data=object_as_dict(update)).dict()
        return JSONResponse(status_code=200, content=response)

    async def like_post(self, post_id, user_id, db):
        post = PostRepo().get_post_by_id(post_id, db)
        if post.owner_id != user_id:
            updated_data = {
                'like': post.like + 1,
                'dislike': post.dislike - 1

            }
            PostRepo().update_post(post_id, updated_data, db)
            response = BaseResponseSchema(status=200, message='Post liked').dict()
            return JSONResponse(status_code=200, content=response)
        else:
            response = BaseResponseSchema(status=200, message='you cant like your posts').dict()
            return JSONResponse(status_code=200, content=response)

    async def dislike_post(self, post_id, user_id, db):
        post = PostRepo().get_post_by_id(post_id, db)
        if post.owner_id != user_id:
            if post.dislike != 0:
                updated_data = {
                    'like': post.like - 1,
                    'dislike': post.dislike + 1
                }
                PostRepo().update_post(post_id, updated_data, db)
                response = BaseResponseSchema(status=200, message='Post disliked').dict()
                return JSONResponse(status_code=200, content=response)
        else:
            response = BaseResponseSchema(status=200, message='you cant dislike your posts').dict()
            return JSONResponse(status_code=200, content=response)
