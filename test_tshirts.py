import unittest
from tshirts import size

class TestTShirtSize(unittest.TestCase):

    def test_size_small(self):
        self.assertEqual(size(36), 'S')
        self.assertEqual(size(37), 'S')
        self.assertEqual(size(38), 'S')

    def test_size_medium(self):
        self.assertEqual(size(39), 'M')
        self.assertEqual(size(40), 'M')
        self.assertEqual(size(41), 'M')

    def test_size_large(self):
        self.assertEqual(size(42), 'L')
        self.assertEqual(size(43), 'L')

    def test_size_extra_large(self):
        self.assertEqual(size(44), 'XL')
        self.assertEqual(size(45), 'XL')

    def test_size_boundary_conditions(self):
        self.assertEqual(size(36), 'S')  # Assuming 36 is the lower boundary for 'S'
        self.assertEqual(size(47), 'XL')  # Assuming 47 is the upper boundary for 'XL'

    def test_size_invalid(self):
        with self.assertRaises(ValueError):
            size(35)  # Assuming 35 is below the valid range
        with self.assertRaises(ValueError):
            size(48)  # Assuming 48 is above the valid range

if __name__ == '__main__':
    unittest.main()