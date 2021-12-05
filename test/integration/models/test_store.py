from models.store import StoreModel
from models.item import ItemModel
from test.base_test import BaseTest


class StoreTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel(name='test')

            self.assertIsNone(obj=StoreModel.find_by_name('test'),
                              msg="Found an store with name 'test' before save_to_db")

            store.save_to_db()

            self.assertIsNotNone(obj=StoreModel.find_by_name('test'),
                                 msg="Did not find an store with name 'test' after save_to_db")

            store.delete_from_db()

            self.assertIsNone(obj=StoreModel.find_by_name('test'),
                              msg="Found an store with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel(name='test')
            item = ItemModel(name='test_item', price=19.99, store_id=1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(first=store.items.count(), second=1)
            self.assertEqual(first=store.items.first().name, second='test_item')
