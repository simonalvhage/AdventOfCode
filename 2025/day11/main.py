import sys

import networkx as nx
sys.path.append("..")
from aoc_helper import InputReader


def part1(data) -> int | None:
    graph = nx.DiGraph()

    for line in data:
        device, outputs = line.split(':')
        for output in outputs.strip().split():
            graph.add_edge(device.strip(), output)
    #solves all paths
    paths = list(nx.all_simple_paths(graph, "you", "out"))
    return len(paths)


def part2(data) -> int | None:
    graph = nx.DiGraph()

    for line in data:
        device, outputs = line.split(':')
        for output in outputs.strip().split():
            graph.add_edge(device.strip(), output)

    seen = {}
    for n in graph.nodes():
        #Tracking of each combination: [seen none, seen dac, seen fft, seen both]
        seen[n] = [0, 0, 0, 0]
    seen["svr"][0] = 1

    #Count paths through graph, tracking if we've passed dac and fft
    for node in nx.topological_sort(graph):
        for neighbor in graph.successors(node):
            if neighbor == "dac":
                seen[neighbor][1] += seen[node][0] + seen[node][1]
                seen[neighbor][3] += seen[node][2] + seen[node][3]
            elif neighbor == "fft":
                seen[neighbor][2] += seen[node][0] + seen[node][2]
                seen[neighbor][3] += seen[node][1] + seen[node][3]
            else:
                for i in range(4):
                    seen[neighbor][i] += seen[node][i]

    #How many seen both dac and fft and passed out
    return seen["out"][3]


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
