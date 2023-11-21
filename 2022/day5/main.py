crate1 = ["P", "V", "Z", "W", "D", "T"]
crate2 = ["D", "J", "F", "V", "W", "S", "L"]
crate3 = ["H", "B", "T", "V", "S", "L", "M", "Z"]
crate4 = ["J", "S", "R"]
crate5 = ["W", "L", "M", "F", "G", "B", "Z", "C"]
crate6 = ["B", "G", "R", "Z", "H", "V", "W", "Q"]
crate7 = ["N", "D", "B", "C", "P", "J", "V"]
crate8 = ["Q", "B", "T", "P"]
crate9 = ["C", "R", "Z", "G", "H"]


def part1():
    with open('input.txt', 'r') as k:
        for items in k.read().splitlines()[10:]:
            numberofmoves = int(items.split(" ")[1])
            fromcrate = "crate" + str(items.split(" ")[3])
            tocrate = "crate" + str(items.split(" ")[5])
            for i in range(numberofmoves):
                globals()[tocrate] = [globals()[fromcrate][0]] + globals()[tocrate]
                globals()[fromcrate] = globals()[fromcrate][1:]
    print("".join(globals()["crate" + str(i)][0] for i in range(1, 10)))


def part2():
    with open('input.txt', 'r') as k:
        for items in k.read().splitlines()[10:]:
            numberofmoves = int(items.split(" ")[1])
            fromcrate = "crate" + str(items.split(" ")[3])
            tocrate = "crate" + str(items.split(" ")[5])
            globals()[tocrate] = globals()[fromcrate][0:numberofmoves] + globals()[tocrate]
            globals()[fromcrate] = globals()[fromcrate][numberofmoves:]
    print("".join(globals()["crate" + str(i)][0] for i in range(1, 10)))


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
