import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    start_column = data[0].index("S")
    beams = {start_column: 1}
    splits = 0
    for row in data[1:]:
        next_beams = {}
        for col in beams:
            if row[col] == ".":
                next_beams[col] = 1
            if row[col] == "^":
                splits += 1
                next_beams[col - 1] = 1
                next_beams[col + 1] = 1
        beams = next_beams
    return splits


def part2(data) -> int | None:
    start_column = data[0].index("S")
    ways = {start_column: 1}
    for row in data[1:]:
        next_way = {}
        for col, count in ways.items():
            if row[col] == ".":
                if col not in next_way:
                    next_way[col] = 0
                next_way[col] += count
            if row[col] == "^":
                if col - 1 not in next_way:
                    next_way[col - 1] = 0
                if col + 1 not in next_way:
                    next_way[col + 1] = 0
                next_way[col - 1] += count
                next_way[col + 1] += count
        ways = next_way

    num_of_ways = sum(ways.values())
    return num_of_ways


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
