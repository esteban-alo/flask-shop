from models.item import ItemModel
from models.store import StoreModel
from test.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel(name='test')
            store.save_to_db()
            item = ItemModel(name='test', price=19.99, store_id=1)

            self.assertIsNone(obj=ItemModel.find_by_name('test'),
                              msg="Found an item with name 'test' before save_to_db")

            item.save_to_db()

            self.assertIsNotNone(obj=ItemModel.find_by_name('test'),
                                 msg="Did not find an item with name 'test' after save_to_db")

            item.delete_from_db()

            self.assertIsNone(obj=ItemModel.find_by_name('test'),
                              msg="Found an item with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel(name='test_store')
            item = ItemModel(name='test', price=19.99, store_id=1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(first=item.store.name, second='test_store')
