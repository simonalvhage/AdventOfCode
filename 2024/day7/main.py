from itertools import product


def read_input(file_path: str) -> list[str]:
	with open(file_path, "r") as file:
		return file.read().strip().splitlines()


def part1(data) -> None:
	total = 0
	operators = ['+', '*']

	for line in data:
		line = line.strip()
		left, right = line.split(':')
		target = int(left.strip())
		numbers = list(map(int, right.strip().split()))

		for op_combination in product(operators, repeat=len(numbers) - 1):
			value = numbers[0]
			for op, next_num in zip(op_combination, numbers[1:]):
				if op == '+':
					value += next_num
				elif op == '*':
					value *= next_num

			if value == target:
				total += target
				break

	print(f"Part 1: {total}")



def part2(data) -> None:
	total = 0
	operators = ['+', '*', '||']

	for line in data:
		line = line.strip()
		left, right = line.split(':')
		target = int(left.strip())
		numbers = list(map(int, right.strip().split()))

		for op_combination in product(operators, repeat=len(numbers) - 1):
			value = numbers[0]
			for op, next_num in zip(op_combination, numbers[1:]):
				if op == '+':
					value += next_num
				elif op == '*':
					value *= next_num
				elif op == '||':
					value = int(str(value) + str(next_num))

			if value == target:
				total += target
				break

	print(f"Part 2: {total}")

if __name__ == "__main__":
	input_file = "input.txt"
	input_data = read_input(input_file)

	print("Advent of Code - Dag 7")
	part1(input_data)
	part2(input_data)
