from zoo import animals
import unittest

class TestFielder(unittest.TestCase):

	def setUp(self):
		pass

	def test_package_zoo_import_animals_length_is_three(self):
		self.assertEqual(len(animals), 3)