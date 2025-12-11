import re


def part1():
    total = 0
    with open('input.txt', 'r') as k:
        for line in k.read().splitlines():
            k = re.findall(r'\d+', line)
            linenumber = str(k[0][0]) + str(k[-1][-1])
            total += int(linenumber)
    print(total)

def part2():
    total = 0
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open('input.txt', 'r') as k:
        for line in k.read().splitlines():
            for x in range(0, len(numbers)):
                try:
                    line = line.replace(numbers[x], numbers[x] + str(x + 1) + numbers[x])
                except:
                    continue
            k = re.findall(r'\d+', line)
            linenumber = str(k[0][0]) + str(k[-1][-1])
            total += int(linenumber)
    print(total)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
