def read_input(file_path: str) -> list[str]:
	with open(file_path, "r") as file:
		return file.read().strip().splitlines()


def part1(data) -> None:
	"""
	Part 1.
	"""
	print(f"Part 1: {None}")


def part2(data) -> None:
	"""
	Part 2.
	"""
	print(f"Part 2: {None}")


if __name__ == "__main__":
	input_file = "input.txt"
	input_data = read_input(input_file)

	print("Advent of Code - Dag X")
	part1(input_data)
	part2(input_data)
