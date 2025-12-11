def part1():
    games = []
    max_red = 12
    max_green = 13
    max_blue = 14
    index = 0
    with open('input.txt', 'r') as k:
        for line in k.read().splitlines():
            index += 1
            parts = line.strip().split(": ")
            possible = True
            for set_info in parts[1].split("; "):
                for cube_info in set_info.split(", "):
                    count, color = cube_info.split()
                    if color == "red" and int(count) > max_red:
                        possible = False
                        break
                    elif color == "green" and int(count) > max_green:
                        possible = False
                        break
                    elif color == "blue" and int(count) > max_blue:
                        possible = False
                        break
            if possible:
                games.append(index)

        sum_games = sum(games)
        print(sum_games)

def part2():
    sum = 0
    with open('input.txt', 'r') as k:
        for line in k.read().splitlines():
            parts = line.strip().split(": ")
            max_red = max_green = max_blue = 0
            for set_info in parts[1].split("; "):
                for cube_info in set_info.split(", "):
                    count, color = cube_info.split()
                    if color == "red" and int(count) > max_red:
                        max_red = int(count)
                    elif color == "green" and int(count) > max_green:
                        max_green = int(count)
                    elif color == "blue" and int(count) > max_blue:
                        max_blue = int(count)
            sum += max_red * max_green * max_blue
        print(sum)

def main():
    part1()
    part2()


if __name__ == '__main__':
    main()