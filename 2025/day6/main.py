import sys
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    operations = data[-1].split()
    results = []

    for line in data[:-1]:
        parts = line.split()
        for i, part in enumerate(parts):
            num = int(part)
            #first number needs to be set :P
            if len(results) <= i:
                results.append(num)
            elif operations[i] == "+":
                results[i] += num
            else:
                results[i] *= num

    sum_of_all = sum(results)

    return sum_of_all


def part2(grid) -> int | None:
    num_cols = len(grid[0])
    sum_of_all = 0
    correct_numbers = []

    for col in range(num_cols + 1):
        digit = ""
        if col < num_cols:
            for row in range(len(grid) - 1):
                if col < len(grid[row]) and grid[row][col] != ' ':
                    digit += grid[row][col]

            if col < len(grid[-1]) and grid[-1][col] in '+*':
                op = grid[-1][col]
        #build correct list ex. [1, 24, 356]
        if digit:
            correct_numbers.append(int(digit))
        #when empty column
        elif correct_numbers:
            if op == '+':
                sum_of_all += sum(correct_numbers)
            else:
                product = 1
                #multiply all correct numbers to eachother since we found the operator
                for n in correct_numbers:
                    product *= n
                sum_of_all += product
            correct_numbers = []
    return sum_of_all


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
