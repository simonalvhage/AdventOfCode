small_alphabet = {chr(i): i - 96 for i in range(97, 123)}
big_alphabet = {chr(i): i - 38 for i in range(65, 91)}


def part1():
    with open('input.txt', 'r') as k:
        big_sum = 0
        for items in k.read().splitlines():
            first = items[:len(items) // 2]
            second = items[len(items) // 2:]
            for i in first:
                if i in second:
                    if i.isupper():
                        big_sum = big_sum + big_alphabet[i]
                    else:
                        big_sum = big_sum + small_alphabet[i]
                    break
    print(big_sum)


def part2():
    with open('input.txt', 'r') as s:
        big_sum = 0
        for items in zip(*[iter(s.read().splitlines())] * 3):
            for j in items[0]:
                if j in items[0] and j in items[1] and j in items[2]:
                    if j.isupper():
                        big_sum = big_sum + big_alphabet[j]
                        break
                    else:
                        big_sum = big_sum + small_alphabet[j]
                        break
    print(big_sum)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
