import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    rows = len(data)
    cols = len(data[0])
    can_be_reached = 0

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '@':
                count_of_nearby = 0

                # Vänster
                if j - 1 >= 0 and data[i][j - 1] == '@':
                    count_of_nearby += 1
                # Höger
                if j + 1 < cols and data[i][j + 1] == '@':
                    count_of_nearby += 1
                # Upp
                if i - 1 >= 0 and data[i - 1][j] == '@':
                    count_of_nearby += 1
                # Ner
                if i + 1 < rows and data[i + 1][j] == '@':
                    count_of_nearby += 1
                # Upp-vänster
                if i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] == '@':
                    count_of_nearby += 1
                # Upp-höger
                if i - 1 >= 0 and j + 1 < cols and data[i - 1][j + 1] == '@':
                    count_of_nearby += 1
                # Ner-vänster
                if i + 1 < rows and j - 1 >= 0 and data[i + 1][j - 1] == '@':
                    count_of_nearby += 1
                # Ner-höger
                if i + 1 < rows and j + 1 < cols and data[i + 1][j + 1] == '@':
                    count_of_nearby += 1

                if count_of_nearby < 4:
                    can_be_reached += 1

    return can_be_reached


def part2(data) -> int | None:
    rows = len(data)
    cols = len(data[0])
    total_removed = 0

    while True:
        removed_this_round = 0
        to_remove = []

        for i, row in enumerate(data):
            for j, char in enumerate(row):
                if char == '@':
                    count_of_nearby = 0

                    # Vänster
                    if j - 1 >= 0 and data[i][j - 1] == '@':
                        count_of_nearby += 1
                    # Höger
                    if j + 1 < cols and data[i][j + 1] == '@':
                        count_of_nearby += 1
                    # Upp
                    if i - 1 >= 0 and data[i - 1][j] == '@':
                        count_of_nearby += 1
                    # Ner
                    if i + 1 < rows and data[i + 1][j] == '@':
                        count_of_nearby += 1
                    # Upp-vänster
                    if i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] == '@':
                        count_of_nearby += 1
                    # Upp-höger
                    if i - 1 >= 0 and j + 1 < cols and data[i - 1][j + 1] == '@':
                        count_of_nearby += 1
                    # Ner-vänster
                    if i + 1 < rows and j - 1 >= 0 and data[i + 1][j - 1] == '@':
                        count_of_nearby += 1
                    # Ner-höger
                    if i + 1 < rows and j + 1 < cols and data[i + 1][j + 1] == '@':
                        count_of_nearby += 1

                    if count_of_nearby < 4:
                        to_remove.append((i, j))
                        removed_this_round += 1

        for i, j in to_remove:
            data[i][j] = '.'

        total_removed += removed_this_round

        if removed_this_round == 0:
            break

    return total_removed


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.char_grid()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
