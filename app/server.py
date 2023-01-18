import sqlalchemy
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy.orm import sessionmaker
from starlette.responses import JSONResponse
from http import HTTPStatus

from app.base_class import Base

from core.configs import Configs, Settings
from sqlalchemy import create_engine

from app.users.models.user_model import Users
from app.posts.models.post import Posts
from core.exceptions import CustomException
from core.schemas import BaseResponseSchema

metadata = sqlalchemy.MetaData()
engine = create_engine(
    Configs.DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():  # new
    Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Social Network"
    )
    return app_


app = create_app()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    err_response = BaseResponseSchema(success=False, status=int(exc.code), message=exc.message,
                                      error_code=exc.error_code)

    return JSONResponse(
        status_code=exc.code,
        content=err_response.dict()
    )


@app.exception_handler(RequestValidationError)
async def custom_exception_handler(request: Request, exc: RequestValidationError):
    err_response = BaseResponseSchema(success=False, status=HTTPStatus.UNPROCESSABLE_ENTITY, message=exc.errors(),
                                      error_code="Field required")
    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content=err_response.dict(),
    )


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "data": {},
            "status": 403,
            "succes": False
        }
    )


@AuthJWT.load_config
def get_config():
    return Settings()


@app.on_event("startup")
async def startup():
    create_tables()
