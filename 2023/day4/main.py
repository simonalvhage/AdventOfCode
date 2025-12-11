def part1():
    with open('input.txt', 'r') as k:
        sum = 0
        linesum = 0
        for i, items in enumerate(k):
            k = items.split("|")
            winning = k[0].split(":")[1].split()
            mylines = k[1].split()
            for value in winning:
                if value in mylines:
                    if linesum == 0:
                        linesum = linesum + 1
                    else:
                        linesum = linesum * 2
            sum = sum + linesum
            linesum = 0
    print(sum)


def part2():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
        occu = [1] * len(lines)
        for i, items in enumerate(lines):
            parts = items.split("|")
            winning = parts[0].split(":")[1].split()
            mylines = parts[1].split()

            matches = 0
            for value in winning:
                if value in mylines:
                    matches += 1

            for j in range(i + 1, i + matches + 1):
                occu[j] += occu[i]

    total = sum(occu)
    print(total)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
