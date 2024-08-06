import unittest
from tshirts import size

class TestTShirtSize(unittest.TestCase):

	def test_size_small(self):
		self.assertEqual(size(37), 'S')
		self.assertEqual(size(38), 'S')
		self.assertEqual(size(40), 'S')

	def test_size_medium(self):
		self.assertEqual(size(42), 'M')

	def test_size_large(self):
		self.assertEqual(size(43), 'L')

if __name__ == '__main__':
	unittest.main()