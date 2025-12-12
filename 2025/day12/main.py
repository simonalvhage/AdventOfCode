import sys
sys.path.append("../")
from aoc_helper import InputReader


def part1(data) -> int:
    both_parts = data.strip().split('\n\n')
    shapes = both_parts[0:6]
    region_block = both_parts[6]
    regions = region_block.split('\n')
    area_of_shapes = []
    for p in shapes:
        area = 0
        area += str(p).count('#')
        area_of_shapes.append(area)

    count = 0
    #Only check if shapes area fit in region area B-)
    for region in regions:
        dimensions = region.split(': ')[0]
        shape_counts = region.split(': ')[1].split()
        width, height = dimensions.split('x')
        region_area = int(width) * int(height)
        total_shape_area = 0
        for i, n in enumerate(shape_counts):
            total_shape_area += area_of_shapes[i] * int(n)

        if total_shape_area <= region_area:
            count += 1
    return count


def part2(data) -> str | None:
    return "Congratulations! You have completed Day 12 and Advent of Code 2025!"


if __name__ == "__main__":
    reader = InputReader("input.txt")
    # data = reader.lines()              # List of strings (default)
    # data = reader.integers()           # List of integers
    # data = reader.int_grid()           # 2D grid of single-digit ints
    # data = reader.char_grid()          # 2D grid of characters
    # data = reader.blocks()             # Groups separated by blank lines
    # data = reader.comma_separated_ints()  # Comma-separated integers
    data = reader.raw
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
