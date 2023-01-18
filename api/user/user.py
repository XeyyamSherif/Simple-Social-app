from fastapi import Depends
from sqlalchemy.orm import Session

from api.user.request.user import SignUp
from app.server import get_db
from fastapi import APIRouter

from app.users.services.user import UserService

user_router = APIRouter()


@user_router.post("/sign_up", tags=["Users"])
async def sign_up(request: SignUp, db: Session = Depends(get_db)):
    return await UserService().create_user(request.mail, request.first_name, request.password, db)
