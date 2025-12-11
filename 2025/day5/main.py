import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    """
    Part 1.
    """
    count = 0
    ranges_section = data.split("\n\n")[0]
    food_ids = data.split("\n\n")[1]

    all_ranges = []
    for food_range in ranges_section.split("\n"):
        start, end = food_range.split("-")
        all_ranges.append((int(start), int(end)))

    for food_id in food_ids.split("\n"):
        if food_id:
            for start, end in all_ranges:
                if start <= int(food_id) <= end:
                    count += 1
                    break
    return count


def part2(data) -> int | None:
    """
    Part 2.
    """
    count = 0
    ranges_section = data.split("\n\n")[0]

    all_ranges = []
    for food_range in ranges_section.split("\n"):
        start, end = food_range.split("-")
        all_ranges.append((int(start), int(end)))

    all_ranges.sort()
    highest_seen = 0

    for start, end in all_ranges:
        #already counted
        if end <= highest_seen:
            continue
        #only count the ranges between our end and highest already counted -ish
        if start <= highest_seen:
            count += end - highest_seen
        # else add our range
        else:
            count += end - start + 1
        if end > highest_seen:
            highest_seen = end

    return count


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.raw

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
