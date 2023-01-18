from fastapi import Depends
from sqlalchemy.orm import Session

from api.auth.requests.auth_request import LogIn
from app.auth.services.auth import AuthService
from app.server import get_db
from fastapi import APIRouter
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter()


@auth_router.post("/log_in", tags=["Auth"])
async def log_in(request: LogIn, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    return await AuthService().log_in(request.mail, request.password, Authorize, db)

