from pathlib import Path


class InputReader:
    """Fast input reader with multiple parsing modes for Advent of Code."""

    def __init__(self, file_path: str = "input.txt"):
        self.file_path = Path(file_path)
        self._raw_content = None

    @property
    def raw(self) -> str:
        """Get raw file content (cached)."""
        if self._raw_content is None:
            self._raw_content = self.file_path.read_text()
        return self._raw_content

    def lines(self, strip: bool = True) -> list[str]:
        """Get lines as list of strings."""
        content = self.raw.strip() if strip else self.raw
        return content.splitlines()

    def integers(self) -> list[int]:
        """Parse all integers in the file (one per line)."""
        return [int(line) for line in self.lines() if line]

    def int_grid(self) -> list[list[int]]:
        """Parse as grid of single-digit integers."""
        return [[int(c) for c in line] for line in self.lines()]

    def char_grid(self) -> list[list[str]]:
        """Parse as grid of characters."""
        return [list(line) for line in self.lines()]

    def blocks(self, separator: str = "") -> list[list[str]]:
        """Split input into blocks separated by blank lines."""
        return [block.split("\n") for block in self.raw.strip().split(f"\n{separator}\n")]

    def comma_separated_ints(self) -> list[int]:
        """Parse comma-separated integers."""
        return [int(x) for x in self.raw.strip().split(",")]

    def as_dict(self, delimiter: str = ":") -> dict[str, str]:
        """Parse as key-value pairs."""
        result = {}
        for line in self.lines():
            if delimiter in line:
                key, value = line.split(delimiter, 1)
                result[key.strip()] = value.strip()
        return result


def read_input(file_path: str = "input.txt") -> list[str]:
    """Simple function to read input as list of lines (backwards compatible)."""
    return Path(file_path).read_text().strip().splitlines()


def part1(data) -> int | None:
    rows = len(data)
    cols = len(data[0])
    can_be_reached = 0

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == '@':
                count_of_nearby = 0

                # Vänster
                if j - 1 >= 0 and data[i][j - 1] == '@':
                    count_of_nearby += 1
                # Höger
                if j + 1 < cols and data[i][j + 1] == '@':
                    count_of_nearby += 1
                # Upp
                if i - 1 >= 0 and data[i - 1][j] == '@':
                    count_of_nearby += 1
                # Ner
                if i + 1 < rows and data[i + 1][j] == '@':
                    count_of_nearby += 1
                # Upp-vänster
                if i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] == '@':
                    count_of_nearby += 1
                # Upp-höger
                if i - 1 >= 0 and j + 1 < cols and data[i - 1][j + 1] == '@':
                    count_of_nearby += 1
                # Ner-vänster
                if i + 1 < rows and j - 1 >= 0 and data[i + 1][j - 1] == '@':
                    count_of_nearby += 1
                # Ner-höger
                if i + 1 < rows and j + 1 < cols and data[i + 1][j + 1] == '@':
                    count_of_nearby += 1

                if count_of_nearby < 4:
                    can_be_reached += 1

    return can_be_reached


def part2(data) -> int | None:
    rows = len(data)
    cols = len(data[0])
    total_removed = 0

    while True:
        removed_this_round = 0
        to_remove = []

        for i, row in enumerate(data):
            for j, char in enumerate(row):
                if char == '@':
                    count_of_nearby = 0

                    # Vänster
                    if j - 1 >= 0 and data[i][j - 1] == '@':
                        count_of_nearby += 1
                    # Höger
                    if j + 1 < cols and data[i][j + 1] == '@':
                        count_of_nearby += 1
                    # Upp
                    if i - 1 >= 0 and data[i - 1][j] == '@':
                        count_of_nearby += 1
                    # Ner
                    if i + 1 < rows and data[i + 1][j] == '@':
                        count_of_nearby += 1
                    # Upp-vänster
                    if i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] == '@':
                        count_of_nearby += 1
                    # Upp-höger
                    if i - 1 >= 0 and j + 1 < cols and data[i - 1][j + 1] == '@':
                        count_of_nearby += 1
                    # Ner-vänster
                    if i + 1 < rows and j - 1 >= 0 and data[i + 1][j - 1] == '@':
                        count_of_nearby += 1
                    # Ner-höger
                    if i + 1 < rows and j + 1 < cols and data[i + 1][j + 1] == '@':
                        count_of_nearby += 1

                    if count_of_nearby < 4:
                        to_remove.append((i, j))
                        removed_this_round += 1

        for i, j in to_remove:
            data[i][j] = '.'

        total_removed += removed_this_round

        if removed_this_round == 0:
            break

    return total_removed


if __name__ == "__main__":
    # Fast mode: use InputReader for optimized parsing
    reader = InputReader("input.txt")

    # Choose your parsing method:
    # data = reader.lines()              # List of strings (default)
    # data = reader.integers()           # List of integers
    # data = reader.int_grid()           # 2D grid of single-digit ints
    # data = reader.char_grid()          # 2D grid of characters
    # data = reader.blocks()             # Groups separated by blank lines
    # data = reader.comma_separated_ints()  # Comma-separated integers
    # data = reader.raw                  # Raw string content

    data = reader.char_grid()

    print("Advent of Code 2025 - Day X")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
