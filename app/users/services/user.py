from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.users.repo.user import UserRepo
from app.utils import Hasher, object_as_dict
from core.schemas import BaseResponseSchema


class UserService:
    async def create_user(self, mail, first_name, password, db: Session):
        hashed_pass = Hasher().get_password_hash(password)
        user = UserRepo().add_user(first_name, mail, hashed_pass, db)
        response = BaseResponseSchema(status=201, data=object_as_dict(user)).dict()
        return JSONResponse(status_code=201, content=response)

    async def get_user_by_mail(self, mail, db: Session):
        user = UserRepo().get_user_by_mail(mail, db)
        return user
