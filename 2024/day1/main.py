def part1(file_path):
    list1, list2 = [], []
    total_size = 0

    with open(file_path, 'r') as file:
        for line in file:
            items = line.split()
            list1.append(int(items[0]))
            list2.append(int(items[1]))

    list1.sort()
    list2.sort()

    for x in range(0, len(list1)):
        total_size += abs(list1[x]-list2[x])

    print(total_size)


def part2(file_path):
    list1, list2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            items = line.split()
            list1.append(int(items[0]))
            list2.append(int(items[1]))

    weighted_sum = 0
    for value in list1:
        count = list2.count(value)
        weighted_sum += count * value

    print(weighted_sum)


def main():
    file_path = 'input.txt'

    part1(file_path)
    part2(file_path)


if __name__ == '__main__':
    main()