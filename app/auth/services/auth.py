from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.users.services.user import UserService
from app.utils import Hasher
from core.exceptions import UserNotFoundException, PasswordDoesNotMatchException
from core.schemas import BaseResponseSchema


class AuthService:

    async def log_in(self, mail, password, Authorize, db: Session):
        user = await UserService().get_user_by_mail(mail, db)
        if user is not None:
            check_pass = Hasher().verify_password(password, user.password)
            if check_pass:
                data = {
                    'acces_token': Authorize.create_access_token(subject=user.id),
                    'refresh_token': Authorize.create_refresh_token(subject=user.id)
                }
                response = BaseResponseSchema(status=200, data=data).dict()
                return JSONResponse(status_code=200, content=response)
            else:
                raise PasswordDoesNotMatchException
        else:
            raise UserNotFoundException
