import factory
from service.models import Item

class ItemFactory(factory.Factory):
    """ Factory for creating fake Items. """

    class Meta:
        model = Item


    id = factory.Sequence(lambda n: n)
    text = factory.Faker('sentence', nb_words=4)
