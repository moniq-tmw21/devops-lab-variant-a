import unittest
from src import password_policy as policy


class PolicyTests(unittest.TestCase):
    def test_combined_requirements(self):
        self.assertEqual(policy.minimum_password_length, 16)
        self.assertTrue(policy.require_numbers)
        self.assertTrue(policy.require_symbols)
