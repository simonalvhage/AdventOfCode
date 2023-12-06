def part1():
    with open('input.txt', 'r') as file:
        k = file.read().splitlines()
    times = k[0].split()[1:]
    record_distances = k[1].split()[1:]

    total_ways = 1

    for i, time in enumerate(times):
        ways = 0
        for duration in range(0, int(time)):
            # speed = duration
            remaining_time = int(time) - duration
            traveled_distance = duration * remaining_time
            if traveled_distance > int(record_distances[i]):
                ways += 1
        total_ways *= ways
    print(total_ways)


def part2():
    with open('input.txt', 'r') as file:
        k = file.read().splitlines()
    times = int(k[0].replace(" ", "").split(":")[1])
    record_distance = int(k[1].replace(" ", "").split(":")[1])

    total_ways = 0

    for duration in range(0, times):
        # speed = duration
        remaining_time = times - duration
        traveled_distance = duration * remaining_time
        if traveled_distance > record_distance:
            total_ways += 1
    print(total_ways)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
