import pytest
from service import app
from service.models import Item, db
from tests.unit_test.factories import ItemFactory


@pytest.fixture(scope='module')
def setup_app():
    """ Fixture for setting up the app and database connection. """
    Item.init_db(app)
    yield

    # tear down
    db.session.remove()

@pytest.fixture(autouse=True)
def cleanup_db():
    """ Fixture for cleaning up the database before each test. """
    with app.app_context():  # Ensure the app context is pushed
        db.session.query(Item).delete()
        db.session.commit()


def test_create_an_item():
    """ It should Create an Account and assert that it exists. """
    fake_item = ItemFactory()
    item = Item(text=fake_item.text)

    assert item is not None
    assert item.id is None
    assert item.text == fake_item.text


def test_add_an_item():
    """ It should add an Item to the database. """
    with app.app_context():
        items = Item.get_all_items()
        assert len(items) == 0

        fake_item = ItemFactory()
        fake_item.add_to_db()

        assert fake_item.id is not None
        items = Item.get_all_items()
        assert len(items) == 1