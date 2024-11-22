from service.extensions import db


class PersistentBase:
    def __init__(self):
        self.id = None


    @classmethod
    def get_all_items(cls):
        """ Returns all the records in the database. """
        return cls.query.all()


    @classmethod
    def find_item_by_id(cls, by_id):
        """ Finds a record by its ID. """
        return cls.query.get(by_id)

    def add_to_db(self):
        """
        Creates an Item and adds it to the database.
        """
        self.id = None  # id must be none to generate next primary key
        db.session.add(self)
        db.session.commit()

    def update_db(self):
        """
        Updates an Item in the database.
        """
        db.session.commit()

    def delete_from_db(self):
        """ Removes an Item from the database. """
        db.session.delete(self)
        db.session.commit()


class Item(db.Model, PersistentBase):
    """
    Class for Item.
    """
    app = None

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Item {self.text}, id: {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
        }
