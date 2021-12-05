from models.item import ItemModel
from test.base_test import BaseTest


class ItemTest(BaseTest):
    def test_create_item(self):
        item = ItemModel(name='test', price=19.99, store_id=1)

        self.assertEqual(first=item.name,
                         second='test',
                         msg="The name of the item after creation does not equal the constructor argument.")

        self.assertEqual(first=item.price,
                         second=19.99,
                         msg="The price of the item after creation does not equal the constructor argument.")

        self.assertEqual(first=item.store_id,
                         second=1,
                         msg="The store_id of the item after creation does not equal the constructor argument.")

        self.assertIsNone(obj=item.store,
                          msg="The item's store was not None even though the store was not created.")

    def test_item_json(self):
        item = ItemModel(name='test', price=19.99, store_id=1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(first=item.json(),
                         second=expected,
                         msg="The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(),
                                                                                                          expected))
