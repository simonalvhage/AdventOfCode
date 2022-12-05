def part1and2():
    with open('input.txt') as f:
        kcal = f.read().splitlines()
        elf = 0
        elfes = []
        for items in kcal:
            if not items:
                elfes.append(elf)
                elf = 0
            if items:
                elf = elf + int(items)
        elfes.sort(reverse=True)
        print(str(elfes[0]) + "\n" + str(sum(elfes[0:3])))


def main():
    part1and2()


if __name__ == '__main__':
    main()
