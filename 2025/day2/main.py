import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    """
    Part 1.
    """
    count = 0
    for code_ranges in data.split(","):
        numbers = code_ranges.split("-")
        start = numbers[0]
        end = numbers[1]
        for number_between in range(int(start), int(end) + 1):
            mid = len(str(abs(number_between))) // 2
            if str(number_between)[:mid] == str(number_between)[mid:]:
                count = count + number_between
    return count


def part2(data) -> int | None:
    """
    Part 2.
    """
    count = 0
    for code_ranges in data.split(","):
        numbers = code_ranges.split("-")
        start = numbers[0]
        end = numbers[1]
        for number_between in range(int(start), int(end) + 1):
            s = str(number_between)
            length = len(s)
            mid = len(str(abs(number_between))) // 2
            for pattern_len in range(1, mid + 1):
                pattern = s[:pattern_len]
                repetitions = int(length / pattern_len)
                if pattern * repetitions == s:
                    count = count + number_between
                    break
    return count


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.raw

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
