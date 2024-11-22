import pytest
from service import create_app, db
from service.extensions import redis_client
from unittest.mock import Mock


@pytest.fixture()
def app():
    app = create_app()

    redis_client.get = Mock(return_value=None)  # Mock `get` to return `None`
    redis_client.set = Mock()  # Mock `set` to do nothing
    redis_client.delete = Mock()



    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
