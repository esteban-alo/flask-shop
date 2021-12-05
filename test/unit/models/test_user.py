from models.user import UserModel
from test.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel(username='test', password='abcd')

        self.assertEqual(first=user.username,
                         second='test',
                         msg="The name of the user after creation does not equal the constructor argument.")

        self.assertEqual(first=user.password,
                         second='abcd',
                         msg="The password of the user after creation does not equal the constructor argument.")
