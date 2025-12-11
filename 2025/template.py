import sys
sys.path.append("../../..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    result = None
    # Your solution here
    return result


def part2(data) -> int | None:
    result = None
    # Your solution here
    return result


if __name__ == "__main__":
    reader = InputReader("input.txt")
    # data = reader.lines()              # List of strings (default)
    # data = reader.integers()           # List of integers
    # data = reader.int_grid()           # 2D grid of single-digit ints
    # data = reader.char_grid()          # 2D grid of characters
    # data = reader.blocks()             # Groups separated by blank lines
    # data = reader.comma_separated_ints()  # Comma-separated integers
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
