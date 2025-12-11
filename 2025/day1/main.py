import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    """
    Part 1.
    """
    current = 50
    zero_count = 0
    for values in data:
        if "R" in values:
            current = current + int(values[1:])
            while current > 99:
                current = current - 100
        if "L" in values:
            current = current - int(values[1:])
            while current < 0:
                current = current + 100
        if current == 0:
            zero_count += 1
        print(current)
                    
    return zero_count


def part2(data) -> int:
    current = 50
    zero_count = 0
    for values in data:
        if "R" in values:
            current = current + int(values[1:])
            while current >= 100:
                current = current - 100
                zero_count += 1
        if "L" in values:
            start = current
            current = current - int(values[1:])
            first = True
            while current < 0:
                current = current + 100
                if first and start == 0:
                    pass
                else:
                    zero_count += 1
                first = False
            if current == 0 and start != 0:
                zero_count += 1
    return zero_count


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
