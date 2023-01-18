import uvicorn

from api.auth.auth import auth_router
from api.posts.posts import post_router
from api.user.user import user_router
from app.server import app

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(post_router)



def main():
    uvicorn.run(
        app="app.server:app",
        reload=True
    )


if __name__ == "__main__":
    main()
