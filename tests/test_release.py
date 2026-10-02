import unittest
from src.release_config import retry_limit, enable_receipts
from src.receipt import receipt_label


class ReleaseTests(unittest.TestCase):
    def test_combined_config(self):
        self.assertEqual(retry_limit, 5)
        self.assertTrue(enable_receipts)

    def test_receipt(self):
        self.assertEqual(receipt_label(42), "Order 42")
