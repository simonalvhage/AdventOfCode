def read_input(file_path: str) -> list[str]:
    rules = []
    pages = []
    with open(file_path, "r") as file:
        sections = file.read().strip().split('\n\n')
        for line in sections[0].split('\n'):
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
        for line in sections[1].split('\n'):
            if line.strip():
                pages.append(list(map(int, line.strip().split(','))))
    sections[0] = rules
    sections[1] = pages
    return sections


def part1(data):
    rules, pages = data
    total = 0
    for instruction in pages:
        correctly_ordered = True
        for rule in rules:
            x, y = rule
            if x in instruction and y in instruction:
                if instruction.index(x) >= instruction.index(y):
                    correctly_ordered = False
                    break
        if correctly_ordered:
            n = len(instruction)
            middle_index = n // 2
            total += instruction[middle_index]
    print(f"Part 1: {total}")

def part2(data):
    rules, pages = data
    total = 0

    for instruction in pages:
        correctly_ordered = True
        for x, y in rules:
            if x in instruction and y in instruction:
                if instruction.index(x) >= instruction.index(y):
                    correctly_ordered = False
                    break

        if not correctly_ordered:
            nodes = set(instruction)
            graph = {node: [] for node in nodes}
            for x, y in rules:
                if x in nodes and y in nodes:
                    graph[x].append(y)

            visited = {}
            stack = []
            def dfs(node):
                if node in visited:
                    return
                visited[node] = 'visiting'
                for neighbor in graph[node]:
                    dfs(neighbor)
                visited[node] = 'visited'
                stack.append(node)

            for node in nodes:
                if node not in visited:
                    dfs(node)

            sorted_instruction = stack[::-1]
            n = len(sorted_instruction)
            middle_index = n // 2
            total += sorted_instruction[middle_index]

    print(f"Part 2: {total}")


if __name__ == "__main__":
    input_file = "input.txt"
    input_data = read_input(input_file)

    print("Advent of Code - Dag 4")
    part1(input_data)
    part2(input_data)
