from fastapi import FastAPI

import view


def create_app():
    app = FastAPI()
    app.include_router(view.router)
    return app
