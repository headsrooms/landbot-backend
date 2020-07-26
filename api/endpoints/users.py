from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import UJSONResponse
from starlette.routing import Route

from api.models import User
from api.schemas import UserResponse


async def users(request: Request) -> UJSONResponse:
    users = await User.all().values()
    users = [UserResponse(**user).as_dict() for user in users]
    return UJSONResponse({"users": users})


async def user(request: Request) -> UJSONResponse:
    user_id = request.path_params["user_id"]
    user = await User.filter(id=user_id).first().values()

    try:
        user = UserResponse(**user[0]).as_dict()
    except IndexError:  # there is no user with such id
        raise HTTPException(
            status_code=404, detail=f"There is no user with id {user_id}"
        )

    return UJSONResponse(user)


routes = [
    Route("/", users, methods=["GET"]),
    Route("/{user_id:uuid}", user, methods=["GET"]),
]
