def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return file.read().splitlines()


def parse_grid(data):
    grid = [list(row) for row in data]
    rows = len(grid)
    cols = len(grid[0])

    start_r, start_c = 0, 0
    direction = '^'
    found = False

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['^', '>', 'v', '<']:
                start_r, start_c = r, c
                direction = grid[r][c]
                grid[r][c] = '.'
                found = True
                break
        if found:
            break

    return grid, rows, cols, start_r, start_c, direction


def simulate(grid, rows, cols, start_r, start_c, direction):
    visited = set()
    r, c = start_r, start_c
    visited.add((r, c))

    while True:
        if direction == '^':
            front_r, front_c = r - 1, c
        elif direction == 'v':
            front_r, front_c = r + 1, c
        elif direction == '<':
            front_r, front_c = r, c - 1
        elif direction == '>':
            front_r, front_c = r, c + 1

        if not (0 <= front_r < rows and 0 <= front_c < cols):
            break

        if grid[front_r][front_c] == '#':
            direction = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]
        else:
            r, c = front_r, front_c
            visited.add((r, c))

    return visited


def simulate_with_obstruction(grid, rows, cols, start_r, start_c, direction, obst_r, obst_c):
    grid[obst_r][obst_c] = '#'
    visited_states = set()
    r, c = start_r, start_c
    d = direction
    visited_states.add((r, c, d))

    while True:
        if d == '^':
            fr, fc = r - 1, c
        elif d == 'v':
            fr, fc = r + 1, c
        elif d == '<':
            fr, fc = r, c - 1
        elif d == '>':
            fr, fc = r, c + 1

        if not (0 <= fr < rows and 0 <= fc < cols):
            grid[obst_r][obst_c] = '.'
            return False

        if grid[fr][fc] == '#':
            d = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[d]
        else:
            r, c = fr, fc

        state = (r, c, d)
        if state in visited_states:
            grid[obst_r][obst_c] = '.'
            return True

        visited_states.add(state)


def part1(data):
    grid, rows, cols, start_r, start_c, direction = parse_grid(data)
    visited = simulate(grid, rows, cols, start_r, start_c, direction)
    print(f"Part 1: {len(visited)}")


def part2(data):
    grid, rows, cols, start_r, start_c, direction = parse_grid(data)
    loop_positions = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) != (start_r, start_c) and grid[r][c] == '.':
                if simulate_with_obstruction(grid, rows, cols, start_r, start_c, direction, r, c):
                    loop_positions += 1

    print(f"Part 2: {loop_positions}")


if __name__ == "__main__":
    input_file = "input.txt"
    input_data = read_input(input_file)
    print("Advent of Code - Dag 6")
    part1(input_data)
    part2(input_data)
