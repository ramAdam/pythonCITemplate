import unittest

class TestStringsDemo(unittest.TestCase):

    def test_integration_demo(self):
        self.assertEqual("jam", "jam", "two strings are not the same")