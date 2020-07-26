import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount
from tortoise.contrib.starlette import register_tortoise

from api import settings
from api.endpoints import questions, users
from api.exception_handlers import exception_handlers
from api.middleware import middleware

routes = [
    Mount("/questions", routes=questions.routes),
    Mount("/users", routes=users.routes),
]

app = Starlette(
    debug=settings.DEBUG,
    routes=routes,
    middleware=middleware,
    exception_handlers=exception_handlers,
)

register_tortoise(
    app,
    db_url=settings.DB_URL,
    modules={"models": ["api.models"]},
    generate_schemas=settings.GENERATE_SCHEMAS,
)

if __name__ == "__main__":
    uvicorn.run(app)
