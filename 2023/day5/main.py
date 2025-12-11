def part1():
    with open('input.txt', 'r') as k:
        k_content = k.read()
        seedss = k_content.splitlines()[0].split(": ")[1].split()
        seeds = [int(seed) for seed in seedss]

        input_sections = k_content.split("\n\n")[1:]

        for x in range(len(input_sections)):
            conversion = input_sections[x].split("\n")[1:]
            for i in range(len(seeds)):
                for h, line in enumerate(conversion):
                    if int(line.split()[1]) <= seeds[i] < int(line.split()[1]) + int(line.split()[2]):
                        seeds[i] = int(line.split()[0]) + (seeds[i] - int(line.split()[1]))
                        break
        print(min(seeds))


def calculate(seed):
    with open('input.txt', 'r') as k:
        k_content = k.read()
        input_sections = k_content.split("\n\n")[1:]

        for x in range(len(input_sections)):
            conversion = input_sections[x].split("\n")[1:]
            for h, line in enumerate(conversion):
                if int(line.split()[1]) <= seed < int(line.split()[1]) + int(line.split()[2]):
                    seed = int(line.split()[0]) + (seed - int(line.split()[1]))
                    break
        return seed


def calculate_backwards(seed, input_sections):
    for x in range(len(input_sections)):
        conversion = input_sections[x].split("\n")[1:]
        for h, line in enumerate(conversion):
            if int(line.split()[0]) <= seed < int(line.split()[0]) + int(line.split()[2]):
                seed = int(line.split()[1]) + (seed - int(line.split()[0]))
                break
    return seed


def find_min():
    with open('input.txt', 'r') as k:
        k_content = k.read()
        mins = []
        seeds_info = k_content.splitlines()[0].split(": ")[1].split()
    for i in range(0, len(seeds_info), 2):
        mins.append(int(seeds_info[i]))

    return calculate(min(mins))


def part2():
    with open('input.txt', 'r') as k:
        k_content = k.read()
        seeds_info = k_content.splitlines()[0].split(": ")[1].split()
        input_sections = k_content.split("\n\n")[1:]
        input_sections.reverse()
        maxmin = find_min()
    for x in range(0, maxmin):
        seednumber = calculate_backwards(x, input_sections)
        for i in range(0, len(seeds_info), 2):
            if int(seeds_info[i]) <= seednumber < (int(seeds_info[i]) + int(seeds_info[i + 1])):
                print(x)
                return


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
