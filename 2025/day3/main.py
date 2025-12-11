import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    """
    Part 1.
    """
    sum = 0
    for row in data:
        biggest_on_line = 0
        for i, first_jolt in enumerate(row):
            for j, second_jolt in enumerate(row):
                if i < j:
                    if int(str(first_jolt)+str(second_jolt)) > biggest_on_line:
                        biggest_on_line = int(str(first_jolt)+str(second_jolt))
        sum = sum + biggest_on_line


    return sum


def part2(data) -> int:
    """
    Part 2.
    """
    sum = 0
    for row in data:
        digits = list(row)

        for numbers_to_remove in range(len(row) - 12):
            for i, digit in enumerate(digits[:-1]):
                if digit < digits[i + 1]:
                    digits.pop(i)
                    break
            else:
                #remove last if row sorted >
                digits.pop()

        sum += int(''.join(digits))
    return sum


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
