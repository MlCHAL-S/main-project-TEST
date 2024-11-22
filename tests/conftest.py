import pytest
from service import create_app, db
from service.extensions import redis_client
from unittest.mock import Mock
from service.extensions import talisman


@pytest.fixture()
def app():
    app = create_app(config_name='testing')

    redis_client.get = Mock(return_value=None)  # Mock `get` to return `None`
    redis_client.set = Mock()  # Mock `set` to do nothing
    redis_client.delete = Mock()

    talisman.force_https = False

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
