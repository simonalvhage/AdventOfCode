from collections import defaultdict

def part1():
	with open('input.txt', 'r') as k:
		directory = defaultdict(int)
		current_dir = []
		total_size = 0
		for line in k.read().splitlines():
			if "$ cd" in line:
				where_to = line.split("$ cd ")[1]
				if where_to == "..":
					current_dir = current_dir[:-1]
				else:
					current_dir.append(where_to)
			else:
				try:
					directory["/".join(current_dir)] += int(line.split()[0])
				except:
					pass

	for keys in sorted(directory.keys(),reverse=True):
		directory["/".join(keys.split("/")[:-1])] += directory[keys]

	for e in directory.values():
		if e < 100000:
			total_size += e

	print(total_size)

	return directory

def part2(directory):
	sizes = []
	free_size = 70000000 - directory["/"]
	needed_size = 30000000 - free_size

	for values in directory.values():
		if values > needed_size:
			sizes.append(values)
	print(min(sizes))

def main():
	directory = part1()
	part2(directory)

if __name__ == '__main__':
	main()