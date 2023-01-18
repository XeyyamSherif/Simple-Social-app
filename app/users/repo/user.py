from sqlalchemy.orm import Session

from app.users.models.user_model import Users
from sqlalchemy.exc import SQLAlchemyError

from core.exceptions import DuplicateEmailOrNicknameException


class UserRepo:

    def add_user(self, name, mail, password, db: Session):
        try:
            user = Users(name=name, mail=mail, password=password)
            db.add(user)
            db.commit()
            return user
        except SQLAlchemyError:
            raise DuplicateEmailOrNicknameException

    def get_user_by_mail(self, mail, db: Session):
        user = db.query(Users).filter(Users.mail == mail).first()
        return user
