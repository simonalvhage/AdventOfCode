import itertools
from math import gcd


def part1():
    word = "AAA"
    i = 0
    with open('input.txt', 'r') as k:
        k = k.read().splitlines()
    instructions = k[0]
    superdict = {}
    for items in k[2:]:
        item = items.split(" = ")
        superdict[item[0]] = [item[1].split(", ")[0][1:], item[1].split(", ")[1][:-1]]
    for char in itertools.cycle(instructions):
        i += 1
        if char == "L":
            word = superdict.get(word)[0]
        elif char == "R":
            word = superdict.get(word)[1]
        if word == "ZZZ":
            break
    print(i)


def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // gcd(x, ans)
    return ans


def part2():
    with open('input.txt', 'r') as k:
        k = k.read().splitlines()
    instructions = k[0]
    superdict = {}
    for items in k[2:]:
        item = items.split(" = ")
        superdict[item[0]] = [item[1].split(", ")[0][1:], item[1].split(", ")[1][:-1]]

    current_nodes = [node for node in superdict if node.endswith('A')]

    T = {}
    steps = 0

    for char in itertools.cycle(instructions):
        for i, node in enumerate(current_nodes):
            if char == "L":
                current_nodes[i] = superdict[node][0]
            elif char == "R":
                current_nodes[i] = superdict[node][1]

            if current_nodes[i].endswith('Z'):
                T[i] = steps + 1
                if len(T) == len(current_nodes):
                    lcm_result = lcm(T.values())
                    print(lcm_result)
                    return
        steps += 1


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
