from service.models import Item
from tests.unit_test.factories import ItemFactory


def test_create_an_item():
    """ It should Create an Item and assert that it exists. """
    fake_item = ItemFactory()
    item = Item(text=fake_item.text)

    assert item is not None
    assert item.id is None
    assert item.text == fake_item.text


def test_add_an_item(app):
    """ It should add an Item to the database. """
    with app.app_context():
        items = Item.get_all_items()
        assert len(items) == 0

        fake_item = ItemFactory()
        fake_item.add_to_db()

        assert fake_item.id is not None
        items = Item.get_all_items()
        assert len(items) == 1

def test_get_all_items(app):
    """ This should get all items from the database. """
    with app.app_context():
        items = Item.get_all_items()
        assert len(items) == 0

        fake_items = [ItemFactory() for _ in range(3)]
        for item in fake_items:
            item.add_to_db()

        items = Item.get_all_items()
        assert len(items) == 3

def test_get_item_by_id(app):
    """ This should get a single item by its ID. """
    with app.app_context():
        fake_items = [ItemFactory() for _ in range(3)]
        for item in fake_items:
            item.add_to_db()

        items = Item.get_all_items()
        assert len(items) == 3

        item = Item.find_item_by_id(fake_items[1].id)
        assert item.id == fake_items[1].id

def test_add_to_db(app):
    """ This should add a new Item to the db. """
    with app.app_context():
        items = Item.get_all_items()
        assert len(items) == 0

        fake_item = ItemFactory()
        fake_item.add_to_db()

        items = Item.get_all_items()
        assert len(items) == 1

def test_update_db(app):
    """ This should update an Item in the db. """
    with app.app_context():
        fake_item = ItemFactory()
        fake_item.add_to_db()

        fake_item.text = 'Updated Text'
        fake_item.update_db()

        items = Item.get_all_items()
        assert len(items) == 1
        assert items[0].text == 'Updated Text'

def test_delete_from_db(app):
    """ This should delete an Item from the db. """
    with app.app_context():
        fake_item = ItemFactory()
        fake_item.add_to_db()

        items = Item.get_all_items()
        assert len(items) == 1

        fake_item.delete_from_db()

        items = Item.get_all_items()
        assert len(items) == 0

def test_repr(app):
    """ This should test printing an object. """
    with app.app_context():
        item = Item(text='hello')
        item.add_to_db()
        expected_repr = f'<Item hello, id: 1>'
        assert repr(item) == expected_repr
