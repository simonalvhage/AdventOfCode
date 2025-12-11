import sys
sys.path.append("..")
from aoc_helper import InputReader
import math


def part1(data) -> int | None:
    pairs = []
    for first_neighbour in data:
        for second_neighbour in data:
            if first_neighbour < second_neighbour:
                dist = math.dist((int(first_neighbour.split(",")[0]), int(first_neighbour.split(",")[1]),
                                  int(first_neighbour.split(",")[2])),
                                 (int(second_neighbour.split(",")[0]), int(second_neighbour.split(",")[1]),
                                  int(second_neighbour.split(",")[2])))
                pairs.append((dist, first_neighbour, second_neighbour))
    pairs.sort()

    circuits = [{first_neighbour} for first_neighbour in data]

    for dist, first_neighbour, second_neighbour in pairs[:1000]:
        for circuit in circuits:
            if first_neighbour in circuit:
                circuit1 = circuit
            if second_neighbour in circuit:
                circuit2 = circuit

        if circuit1 is not circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

    sizes = []
    for c in circuits:
        sizes.append(len(c))
    sizes.sort(reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


def part2(data) -> int | None:
    pairs = []
    for first_neighbour in data:
        for second_neighbour in data:
            if first_neighbour < second_neighbour:
                dist = math.dist((int(first_neighbour.split(",")[0]), int(first_neighbour.split(",")[1]),
                                  int(first_neighbour.split(",")[2])),
                                 (int(second_neighbour.split(",")[0]), int(second_neighbour.split(",")[1]),
                                  int(second_neighbour.split(",")[2])))
                pairs.append((dist, first_neighbour, second_neighbour))
    pairs.sort()

    circuits = [{first_neighbour} for first_neighbour in data]

    for dist, first_neighbour, second_neighbour in pairs:
        for circuit in circuits:
            if first_neighbour in circuit:
                circuit1 = circuit
            if second_neighbour in circuit:
                circuit2 = circuit

        if circuit1 is not circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

            if len(circuits) == 1:
                x1 = int(first_neighbour.split(",")[0])
                x2 = int(second_neighbour.split(",")[0])
                return x1 * x2


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
