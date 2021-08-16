from fastapi import FastAPI

from markets import view


def create_app():
    app = FastAPI()
    app.include_router(view.router)
    return app
