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

def part2():
    with open('input.txt', 'r') as k:
        k_content = k.read()
        seeds_info = k_content.splitlines()[0].split(": ")[1].split()
        seeds = []
        for i in range(0, len(seeds_info), 2):
            start = int(seeds_info[i])
            length = int(seeds_info[i + 1])
            seeds.extend(range(start, start + length))

        input_sections = k_content.split("\n\n")[1:]

        for x in range(len(input_sections)):
            conversion = input_sections[x].split("\n")[1:]
            for i in range(len(seeds)):
                for h, line in enumerate(conversion):
                    if int(line.split()[1]) <= seeds[i] < int(line.split()[1]) + int(line.split()[2]):
                        seeds[i] = int(line.split()[0]) + (seeds[i] - int(line.split()[1]))
                        break

        print(min(seeds))

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()