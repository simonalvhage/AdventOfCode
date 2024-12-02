def read_input(file_path: str) -> list[str]:
	with open(file_path, "r") as file:
		return file.read().strip().splitlines()


def check_safe(line):
	levels = list(map(int, line.split()))
	increasing = True
	decreasing = True

	for i in range(len(levels) - 1):
		diff = levels[i + 1] - levels[i]
		if not (1 <= diff <= 3):
			increasing = False
		if not (1 <= -diff <= 3):
			decreasing = False

	if increasing or decreasing:
		return 1


def check_safe_with_remove(line, max_removals=1):
	levels = list(map(int, line.split()))

	increasing = True
	decreasing = True

	for i in range(len(levels) - 1):
		diff = levels[i + 1] - levels[i]
		if not (1 <= diff <= 3):
			increasing = False
		if not (1 <= -diff <= 3):
			decreasing = False

	if increasing or decreasing:
		return 1

	if max_removals > 0:
		for i in range(len(levels)):
			new_levels = []
			for j in range(len(levels)):
				if j != i:
					new_levels.append(levels[j])
			if check_safe_with_remove(" ".join(map(str, new_levels)), max_removals - 1):
				return 1

def part1(data) -> None:
	"""
	Part 1.
	"""
	safe_count = 0
	for line in data:
		if check_safe(line):
			safe_count += 1

	print(f"Part 1: {safe_count}")


def part2(data) -> None:
	"""
	Part 2.
	"""
	safe_count = 0
	for line in data:
		if check_safe_with_remove(line):
			safe_count += 1

	print(f"Part 2: {safe_count}")


if __name__ == "__main__":
	input_file = "input.txt"
	input_data = read_input(input_file)

	print("Advent of Code - Dag 2")
	part1(input_data)
	part2(input_data)
