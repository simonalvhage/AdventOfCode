import re

def read_input(file_path: str) -> str:
	with open(file_path, "r") as file:
		return file.read()


def part1(data) -> None:
	"""
	Part 1.
	"""
	sum = 0
	pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
	matches = re.findall(pattern, data)

	for x,y in matches:
		sum += int(x) * int(y)
	print(f"Part 1: {sum}")


def part2(data) -> None:
	"""
	Part 2.
	"""
	sum = 0
	pattern = r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))'
	do = True
	matches = re.findall(pattern, data)
	for match in matches:
		if "do()" in match[0]:
			do = True
		if "don't()" in match[0]:
			do = False
		if do and match[1] and match[2]:
			sum += int(match[1]) * int(match[2])

	print(f"Part 2: {sum}")


if __name__ == "__main__":
	input_file = "input.txt"
	input_data = read_input(input_file)

	print("Advent of Code - Dag 3")
	part1(input_data)
	part2(input_data)
