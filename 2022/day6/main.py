def part1():
    with open('input.txt', 'r') as k:
        items = k.read()
        count = 4
        for i in range(len(items)):
            if not len(set(items[count - 4:count])) == len(items[count - 4:count]):
                count += 1
            else:
                break
    print(count)


def part2():
    with open('input.txt', 'r') as k:
        items = k.read()
        count = 14
        for i in range(len(items)):
            if not len(set(items[count - 14:count])) == len(items[count - 14:count]):
                count += 1
            else:
                break
    print(count)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
