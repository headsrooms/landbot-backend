import pytest
from starlette.testclient import TestClient

from api.app import app


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as test_client:
        yield test_client