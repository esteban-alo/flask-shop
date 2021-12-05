from models.store import StoreModel
from test.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel(name='test')

        self.assertEqual(first=store.name,
                         second='test',
                         msg="The name of the store after creation does not equal the constructor argument.")

        self.assertListEqual(list1=store.items.all(),
                             list2=[],
                             msg="The store's items length was not 0 even though no items were added.")

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertEqual(
            first=store.json(),
            second=expected,
            msg="The JSON export of the store is incorrect. Received {}, expected {}.".format(store.json(), expected))
