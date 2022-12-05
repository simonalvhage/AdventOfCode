def part1():
    with open('input.txt', 'r') as k:
        count = 0
        for items in k.read().splitlines():
            item1 = items.split(',')[0]
            item2 = items.split(',')[1]
            item1list = list(range(int(item1.split('-')[0]), int(item1.split('-')[1]) + 1))
            item2list = list(range(int(item2.split('-')[0]), int(item2.split('-')[1]) + 1))
            if all(x in item1list for x in item2list):
                count = count + 1
            elif all(x in item2list for x in item1list):
                count = count + 1
        print(count)


def part2():
    with open('input.txt', 'r') as k:
        count = 0
        for items in k.read().splitlines():
            item1 = items.split(',')[0]
            item2 = items.split(',')[1]
            item1list = list(range(int(item1.split('-')[0]), int(item1.split('-')[1]) + 1))
            item2list = list(range(int(item2.split('-')[0]), int(item2.split('-')[1]) + 1))
            if any(x in item1list for x in item2list):
                count = count + 1
            elif any(x in item2list for x in item1list):
                count = count + 1
        print(count)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
