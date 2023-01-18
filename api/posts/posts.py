from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from api.posts.requests.post_requests import CreatePost
from app.posts.services.posts import PostService
from app.server import get_db
from fastapi import APIRouter

post_router = APIRouter()


@post_router.post("/create_post", tags=["Posts"])
async def create_post(request: CreatePost, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    # Authorize.jwt_required()
    data = request.dict()
    data['owner_id'] = Authorize.get_jwt_subject()
    return await PostService().create_post(data, db)


@post_router.delete("/delete_post", tags=["Posts"])
async def delete_post(_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return await PostService().delete_post(_id, db)


@post_router.get("/read_posts", tags=["Posts"])
async def read_posts(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return await PostService().read_all_posts(db)


@post_router.patch("/update_post", tags=["Posts"])
async def update_post(_id: int, updated_data: dict, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return await PostService().update_post(_id, updated_data, db)


@post_router.patch("/like_post", tags=["Posts"])
async def like_post(post_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return await PostService().like_post(post_id, Authorize.get_jwt_subject(), db)

@post_router.patch("/dislike_post", tags=["Posts"])
async def dislike_post(post_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return await PostService().dislike_post(post_id, Authorize.get_jwt_subject(), db)
