def part1():
    def check_and_add(row, col, current_char, next_char, direction):
        if current_char in direction and 0 <= row < len(lines) and 0 <= col < len(lines[0]) \
                and lines[row][col] in next_char and (row, col) not in visited:
            queue.append((row, col))
            visited.add((row, col))

    with open("input.txt") as f:
        data = f.read()
        lines = data.splitlines()
        start_index = data.find("S")
        S = divmod(start_index, len(lines[0]))

    queue = [S]
    visited = set()

    while queue:
        row, column = queue.pop(0)

        # Check each direction: UP, DOWN, LEFT, RIGHT
        check_and_add(row - 1, column, lines[row][column], "S|F7", "S|LJ")  # UP
        check_and_add(row + 1, column, lines[row][column], "S|LJ", "S|F7")  # DOWN
        check_and_add(row, column - 1, lines[row][column], "S-LF", "S-J7")  # LEFT
        check_and_add(row, column + 1, lines[row][column], "S-J7", "S-LF")  # RIGHT

    print(len(visited) // 2)


def flood_fill(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in visited or grid[x][y] != '.':
        return
    visited.add((x, y))
    flood_fill(grid, x + 1, y, visited)
    flood_fill(grid, x - 1, y, visited)
    flood_fill(grid, x, y + 1, visited)
    flood_fill(grid, x, y - 1, visited)


def part2():
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    visited = set()

    for i in range(len(grid)):
        flood_fill(grid, i, 0, visited)
        flood_fill(grid, i, len(grid[0]) - 1, visited)
    for j in range(len(grid[0])):
        flood_fill(grid, 0, j, visited)
        flood_fill(grid, len(grid) - 1, j, visited)

    enclosed_count = sum(
        1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '.' and (i, j) not in visited)

    print(enclosed_count)


if __name__ == '__main__':
    part1()
    part2()
