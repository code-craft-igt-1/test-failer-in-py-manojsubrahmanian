def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j} | {major} | {minor}')
    return color_map

def test_all_colors_in_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = get_color_map()
    index = 1
    
    for entry in color_map:
        parts = entry.split('|')
        pair_number = int(parts[0].strip())
        major_color = parts[1].strip()
        minor_color = parts[2].strip()
        
        assert pair_number == index, f"Pair number {pair_number} is not correct, expected {index}"
        assert major_color in major_colors, f"{major_color} is not in the major colors list"
        assert minor_color in minor_colors, f"{minor_color} is not in the minor colors list"
        index += 1

color_map = get_color_map()
assert (len(color_map) == 25)
test_all_colors_in_map()
print("All is well (maybe!)\n")
