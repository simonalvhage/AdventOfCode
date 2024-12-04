def read_input(file_path: str) -> list[str]:
	with open(file_path, "r") as file:
		return file.read().strip().splitlines()


def part1(data):
	count = 0
	rows = len(data)
	cols = len(data[0])
	word = "XMAS"
	word_length = len(word)

	for row in range(rows):
		for col in range(cols):

			# Up
			found = True
			for i in range(word_length):
				new_row = row - i
				new_col = col
				if new_row >= 0:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Down
			found = True
			for i in range(word_length):
				new_row = row + i
				new_col = col
				if new_row < rows:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Left
			found = True
			for i in range(word_length):
				new_row = row
				new_col = col - i
				if new_col >= 0:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Right
			found = True
			for i in range(word_length):
				new_row = row
				new_col = col + i
				if new_col < cols:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Up-left
			found = True
			for i in range(word_length):
				new_row = row - i
				new_col = col - i
				if new_row >= 0 and new_col >= 0:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Up-right
			found = True
			for i in range(word_length):
				new_row = row - i
				new_col = col + i
				if new_row >= 0 and new_col < cols:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Down-left
			found = True
			for i in range(word_length):
				new_row = row + i
				new_col = col - i
				if new_row < rows and new_col >= 0:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

			# Down-right
			found = True
			for i in range(word_length):
				new_row = row + i
				new_col = col + i
				if new_row < rows and new_col < cols:
					if data[new_row][new_col] != word[i]:
						found = False
						break
				else:
					found = False
					break
			if found:
				count += 1

	print("Part 1:", count)


def part2(grid):
	count = 0
	rows = len(grid)
	cols = len(grid[0])
	word = "MAS"
	word_backwards = "SAM"

	for row in range(1, rows - 1):
		for col in range(1, cols - 1):

			# top left -> bottom right
			char1 = grid[row - 1][col - 1]
			char2 = grid[row][col]
			char3 = grid[row + 1][col + 1]
			diag1_word = char1 + char2 + char3

			# top right -> bottom left
			char1 = grid[row - 1][col + 1]
			char2 = grid[row][col]
			char3 = grid[row + 1][col - 1]
			diag2_word = char1 + char2 + char3

			if diag1_word == word or diag1_word == word_backwards:
				if diag2_word == word or diag2_word == word_backwards:
					count += 1

	print("Part 2:", count)


if __name__ == "__main__":
	input_file = "input.txt"
	input_data = read_input(input_file)

	print("Advent of Code - Dag 4")
	part1(input_data)
	part2(input_data)