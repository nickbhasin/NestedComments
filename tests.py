import pytest
import pytest_asyncio
from quart import Quart

from app import app


@pytest_asyncio.fixture(name="test_app", scope="function")
async def test_app():
    async with app.test_app() as test_app:
        yield test_app



@pytest.mark.asyncio
async def test_create_user(test_app: Quart) -> None:
    test_client = test_app.test_client()
    response = await test_client.post("/social_network/userregistration/", json={"name": "test_name"})
    assert response.status_code == 200
    data = await response.get_json()
    assert "id" in data
    assert data["name"] == "test_name"


@pytest.mark.asyncio
async def test_create_user_failure(test_app: Quart) -> None:
    test_client = test_app.test_client()
    response = await test_client.post("/social_network/userregistration/", json={"nam": "test_name"})
    assert response.status_code == 400