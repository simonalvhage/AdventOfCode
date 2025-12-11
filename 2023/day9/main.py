def calc_differences(seq):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i + 1] - seq[i])
    return new_seq


def part1_and_2(reversed = False):
    sum = 0
    with open('input.txt', 'r') as k:
        for items in k.read().splitlines():
            _list = [[int(s) for s in items.split()]]
            if reversed:
                _list[0].reverse()

            while len(set(_list[-1])) != 1:
                _list.append(calc_differences(_list[-1]))

            next_number = _list[-1][0]
            for i in range(len(_list) - 2, -1, -1):
                next_number += _list[i][-1]
            sum += next_number
        print(sum)


def main():
    part1_and_2()
    part1_and_2(True)


if __name__ == '__main__':
    main()
