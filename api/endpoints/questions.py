import os
from dataclasses import asdict

from starlette.background import BackgroundTask
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import UJSONResponse
from starlette.routing import Route
from starlette.status import HTTP_201_CREATED

from api import settings
from api.mailing import send_welcome_email
from api.models import Question, User
from api.schemas import UserInput, QuestionInput, QuestionResponse


async def get_questions(request: Request) -> UJSONResponse:
    questions = await Question.all().values()
    questions = [QuestionResponse(**question).as_dict() for question in questions]
    return UJSONResponse({"questions": questions})


async def post_question(request: Request) -> UJSONResponse:
    payload = await request.json()
    user_data = UserInput(
        payload.get("name"),
        payload.get("last_name"),
        payload.get("email"),
        payload.get("phone"),
    )
    defaults = asdict(user_data)
    del defaults["email"]
    user, created = await User.get_or_create(email=user_data.email, defaults=defaults)

    question_data = QuestionInput(payload.get("question"), user.id)
    question = await Question.create(**asdict(question_data))
    payload["id"] = str(question.id)
    payload["user_id"] = str(user.id)

    task = BackgroundTask(
        send_welcome_email,
        to_address=payload.get("email"),
        username=f"{payload.get('name')} {payload.get('last_name')}",
        bypass=os.getenv("CI") or settings.DEBUG
    )
    return UJSONResponse(payload, status_code=HTTP_201_CREATED, background=task)


async def get_question(request: Request) -> UJSONResponse:
    question_id = request.path_params["question_id"]
    question = await Question.filter(id=question_id).first().values()

    try:
        question = QuestionResponse(**question[0]).as_dict()
    except IndexError:  # there is no question with such id
        raise HTTPException(
            status_code=404, detail=f"There is no question with id {question_id}"
        )

    return UJSONResponse(question)


routes = [
    Route("/", get_questions, methods=["GET"]),
    Route("/", post_question, methods=["POST"]),
    Route("/{question_id:uuid}", get_question, methods=["GET"]),
]
