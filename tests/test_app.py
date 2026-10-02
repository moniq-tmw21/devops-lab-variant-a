import unittest
from decimal import Decimal
from src.payment import calculate_total
from src.auth import authenticate


class PaymentTests(unittest.TestCase):
    def test_multiple_items(self):
        self.assertEqual(calculate_total("19.99", 3), Decimal("59.97"))

    def test_single_item(self):
        self.assertEqual(calculate_total("12.50", 1), Decimal("12.50"))

    def test_rounding(self):
        self.assertEqual(calculate_total("0.335", 3), Decimal("1.01"))

    def test_invalid_price(self):
        for price in ["-1", "NaN", "Infinity"]:
            with self.subTest(price=price), self.assertRaises(ValueError):
                calculate_total(price, 1)

    def test_invalid_quantity(self):
        for quantity in [0, -1, 1.5, True]:
            with self.subTest(quantity=quantity), self.assertRaises(ValueError):
                calculate_total("1", quantity)


class AuthenticationTests(unittest.TestCase):
    def test_valid_user(self):
        self.assertTrue(authenticate("alice", "lab-pass", {"alice": "lab-pass"}))

    def test_wrong_password(self):
        self.assertFalse(authenticate("alice", "wrong", {"alice": "lab-pass"}))

    def test_unknown_user(self):
        self.assertFalse(authenticate("bob", "lab-pass", {"alice": "lab-pass"}))
