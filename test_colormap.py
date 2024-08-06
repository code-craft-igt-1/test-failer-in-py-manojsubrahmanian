import unittest
from colormap import get_color_map

class TestColorMap(unittest.TestCase):

	def test_all_colors_in_map(self):
		major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
		minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
		color_map = get_color_map()
		index = 1

		for entry in color_map:
			parts = entry.split('|')
			pair_number = int(parts[0].strip())
			major_color = parts[1].strip()
			minor_color = parts[2].strip()

			self.assertEqual(pair_number, index, f"Pair number {pair_number} is not correct, expected {index}")
			self.assertIn(major_color, major_colors, f"{major_color} is not in the major colors list")
			self.assertIn(minor_color, minor_colors, f"{minor_color} is not in the minor colors list")
			index += 1

	def test_color_map_length(self):
		color_map = get_color_map()
		self.assertEqual(len(color_map), 25)

if __name__ == '__main__':
	unittest.main()