import re

def is_symbol_nearby(startX, startY, length, grid):
    for i in range(-1, 2):
        for j in range(-1, length + 1):
            x = startX + j
            y = startY + i
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if not grid[y][x].isdigit() and grid[y][x] != '.':
                    return True
    return False


def part1():
    numbers_positions = []
    sum = 0

    grid = [line.strip() for line in open('input.txt', 'r').readlines()]
    for line in grid:
        numbers_in_line = []
        current_number = ""
        current_index = 0

        for index, char in enumerate(line):
            if char.isdigit():
                current_number += char
                if index == len(line) - 1 or not line[index + 1].isdigit():
                    numbers_in_line.append([current_index, len(current_number), int(current_number)])
                    current_number = ""
            else:
                current_index = index + 1

        numbers_positions.append(numbers_in_line)

    for y, row in enumerate(numbers_positions):
        for number_info in row:
            if is_symbol_nearby(number_info[0], y, number_info[1], grid):
                sum += number_info[2]

    print(sum)


def find_numbers_around_gear(startX, startY, grid):
    numbers = []

    # Check horizontally and vertically for numbers adjacent to '*'
    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = startX + x
        ny = startY + y
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx].isdigit():
            num = grid[ny][nx]
            expand_x = x
            expand_y = y
            while 0 <= nx + expand_x < len(grid[0]) and 0 <= ny + expand_y < len(grid) and grid[ny + expand_y][
                nx + expand_x].isdigit():
                nx += expand_x
                ny += expand_y
                num += grid[ny][nx]
            numbers.append(int(num))
    return list(set(numbers)) if len(set(numbers)) == 2 else []


def FindSymbols(startX: int, startY: int, lenght: int, value: int, inputList, gearsFound):
    for i in range(-1, 2):
        row = ''
        for j in range(-1, lenght + 1):
            if (0 <= startY + i < len(inputList) and 0 <= startX + j < len(
                    inputList[startY + i])):
                if re.match(r'[\*]', inputList[startY + i][startX + j]):
                    key = fr'{startY + i},{startX + j}'
                    if key in gearsFound:
                        gearsFound[key].append(value)
                    else:
                        gearsFound[key] = [value]
def part2():
    inputList = []
    numPositions = []
    gearsFound = {}
    grid = [line.strip() for line in open('input.txt', 'r').readlines()]
    for x in grid:
        inputList.append(x)
        tempList = []
        for y in re.finditer(r"\d+", x):
            z = [y.start(), int(y.end() - y.start()), int(y.group())]
            tempList.append(z)
        numPositions.append(tempList)

    for index, posRow in enumerate(numPositions):
        for numInfo in posRow:
            FindSymbols(numInfo[0], index, numInfo[1], numInfo[2], inputList, gearsFound)

    total = 0

    for k in gearsFound:
        if len(gearsFound[k]) == 2:
            total += gearsFound[k][0] * gearsFound[k][1]
    print(total)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()