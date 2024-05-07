import unittest
from unittest.mock import Mock, patch
from olx import Users
from olx.models import AuthenticatedUser


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.users = Users()
        self.mock_get = patch.object(self.users, "get").start()
        # self.mock_get.start()

    def tearDown(self):
        self.mock_get.stop()

    def _mock_response(self, data):
        mock_response = Mock()
        mock_response.json.return_value = {"data": data}
        return mock_response

    def test_get_authenticated_user(self):
        mock_data = {
            "id": 123,
            "email": "john@mail.com",
            "status": "confirmed",
            "name": "John",
            "phone": 123123123,
            "phone_login": 123123123,
            "created_at": "2018-01-29 14:04:13",
            "last_login_at": "2018-01-30 08:20:28",
            "avatar": None,
            "is_business": True,
        }
        self.mock_get.return_value = self._mock_response(mock_data)

        authenticated_user = self.users.get_authenticated_user()

        self.assertIsInstance(authenticated_user, AuthenticatedUser)
        self.assertEqual(authenticated_user.id, 123)
        self.assertEqual(authenticated_user.email, "john@mail.com")
        self.assertEqual(authenticated_user.status, "confirmed")
        self.assertEqual(authenticated_user.name, "John")
        self.assertEqual(authenticated_user.phone, 123123123)
        self.assertEqual(authenticated_user.phone_login, 123123123)
        self.assertEqual(authenticated_user.created_at, "2018-01-29 14:04:13")
        self.assertEqual(authenticated_user.last_login_at, "2018-01-30 08:20:28")
        self.assertIsNone(authenticated_user.avatar)
        self.assertTrue(authenticated_user.is_business)

    def test_get_user(self):
        mock_data = {"id": 1, "name": "John", "avatar": None}
        self.mock_get.return_value = self._mock_response(mock_data)

        user = self.users.get_user(user_id=1)

        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "John")
        self.assertIsNone(user.avatar)

    def test_account_balance(self):
        mock_data = {
            "sum": 6988.02,
            "wallet": 6988.02,
            "bonus": 0,
            "refund": 0,
            "currency": "PLN",
        }
        self.mock_get.return_value = self._mock_response(mock_data)

        account_balance = self.users.account_balance()

        self.assertEqual(account_balance.sum, 6988.02)
        self.assertEqual(account_balance.wallet, 6988.02)
        self.assertEqual(account_balance.bonus, 0)
        self.assertEqual(account_balance.refund, 0)
        self.assertEqual(account_balance.currency, "PLN")

    def test_payment_methods(self):
        mock_data = ["account", "postpaid"]
        self.mock_get.return_value = self._mock_response(mock_data)

        payment_methods = self.users.payment_methods()

        self.assertListEqual(payment_methods, mock_data)


if __name__ == "__main__":
    unittest.main()
