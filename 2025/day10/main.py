import sys
sys.path.append("..")
from scipy.optimize import LinearConstraint, milp
from aoc_helper import InputReader


def part1(data) -> int | None:
    result = 0
    for line in data:
        min_presses = 9999
        test_indicator = []
        indicator = line.split(" ")[0]
        schematics = line.split(" ")[1:-1]
        j_requirements = line.split(" ")[-1]
        list_indicator = list(indicator)[1:-1]
        list_schematics = [[int(item) for item in list(s)[1:-1] if item != ","] for s in schematics]

        for mask in range(2 ** len(list_schematics)):
            test_indicator = ['.'] * len(list_indicator)
            presses = 0

            for button in range(len(list_schematics)):
                if mask & (1 << button):
                    presses += 1
                    for light_idx in list_schematics[button]:
                        if test_indicator[light_idx] == '.':
                            test_indicator[light_idx] = '#'
                        else:
                            test_indicator[light_idx] = '.'

            if test_indicator == list_indicator:
                if presses < min_presses:
                    min_presses = presses
        result += min_presses
    return result


def part2(data) -> int:
    result = 0
    for line in data:
        schematics = line.split(" ")[1:-1]
        j_requirements = line.split(" ")[-1]

        # Fix: använd split för båda
        list_schematics = [[int(x) for x in s[1:-1].split(",")] for s in schematics]
        list_j_requirements = [int(x) for x in j_requirements[1:-1].split(",")]

        equation = [[0] * len(list_schematics) for req in range(len(list_j_requirements))]
        for i, row in enumerate(equation):
            for col in range(len(list_schematics)):
                if i in list_schematics[col]:
                    row[col] = 1

        c = [1] * len(list_schematics)
        #Defines the terms of the milp equation solver, like lb <= A @ x <= ub (kinda :P)
        constraints = LinearConstraint(equation, list_j_requirements, list_j_requirements)
        #Minimize c to the constraints like 1*x0 + 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5
        res = milp(c, constraints=constraints, integrality=c)
        result += int(res.fun)

    return result


if __name__ == "__main__":
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
