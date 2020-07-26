import asyncio
from dataclasses import asdict
from typing import List, Tuple, Dict

import pytest
from faker import Faker
from starlette.testclient import TestClient
from tortoise.transactions import in_transaction

from api.app import app
from api.models import User, Question
from api.schemas import UserInput, QuestionInput


@pytest.yield_fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def client(request):
    with TestClient(app) as c:
        yield c


def user_data():
    faker = Faker()
    return UserInput(
        faker.first_name(), faker.last_name(), faker.email(), faker.phone_number(),
    )


@pytest.mark.asyncio
@pytest.fixture
async def random_user():
    user = await User.create(**asdict(user_data()))
    yield user

    await user.delete()


@pytest.mark.asyncio
@pytest.fixture
async def random_question(random_user: User):
    faker = Faker()
    question_data = QuestionInput(faker.paragraph(), random_user.id)
    question = await Question.create(**asdict(question_data))

    yield question

    await question.delete()


@pytest.mark.asyncio
@pytest.fixture(scope="session", params=[1000])
async def random_users(request):
    async def fin():
        async with in_transaction() as connection:
            for user in users_db:
                await user.delete(using_db=connection)

    users_db = []
    users = []
    request.addfinalizer(fin)

    async with in_transaction() as connection:
        for _ in range(request.param):
            user_d = user_data()
            user = User(**asdict(user_d))
            await user.save(using_db=connection)
            users_db.append(user)
            users.append(asdict(user_d))

    yield users_db, users


@pytest.mark.asyncio
@pytest.fixture(scope="session")
async def random_questions(request, random_users: Tuple[List[User], List[Dict]]):
    async def fin():
        async with in_transaction() as connection:
            for question in questions_db:
                await question.delete(using_db=connection)

    faker = Faker()
    questions = []
    questions_db = []

    request.addfinalizer(fin)
    users_db, users = random_users

    async with in_transaction() as connection:
        for user in users_db:
            question_data = QuestionInput(faker.paragraph(), user.id)
            question = Question(**asdict(question_data))
            await question.save(using_db=connection)
            questions_db.append(question)
            questions.append(asdict(question_data))

    yield questions


@pytest.fixture(scope="session")
def post_question(client):
    faker = Faker()
    payload = {
        "name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "phone": faker.phone_number(),
        "question": faker.paragraph(),
    }
    question = client.post("/questions/", json=payload)
    question = question.json()

    yield payload, question
