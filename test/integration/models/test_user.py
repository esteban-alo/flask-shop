from models.user import UserModel
from test.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNone(obj=UserModel.find_by_username('test'),
                              msg="Found an user with name 'test' before save_to_db")

            self.assertIsNone(obj=UserModel.find_by_id(1),
                              msg="Found an user with id '1' before save_to_db")

            user.save_to_db()

            self.assertIsNotNone(obj=UserModel.find_by_username('test'),
                                 msg="Did not find an user with name 'test' after save_to_db")

            self.assertIsNotNone(obj=UserModel.find_by_id(1),
                                 msg="Did not find an user with id '1' after save_to_db")
