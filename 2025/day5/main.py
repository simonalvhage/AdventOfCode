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
    """
    Part 1.
    """
    count = 0
    ranges_section = data.split("\n\n")[0]
    food_ids = data.split("\n\n")[1]

    all_ranges = []
    for food_range in ranges_section.split("\n"):
        start, end = food_range.split("-")
        all_ranges.append((int(start), int(end)))

    for food_id in food_ids.split("\n"):
        if food_id:
            for start, end in all_ranges:
                if start <= int(food_id) <= end:
                    count += 1
                    break
    return count


def part2(data) -> int | None:
    """
    Part 2.
    """
    count = 0
    ranges_section = data.split("\n\n")[0]

    all_ranges = []
    for food_range in ranges_section.split("\n"):
        start, end = food_range.split("-")
        all_ranges.append((int(start), int(end)))

    all_ranges.sort()
    highest_seen = 0

    for start, end in all_ranges:
        #already counted
        if end <= highest_seen:
            continue
        #only count the ranges between our end and highest already counted -ish
        if start <= highest_seen:
            count += end - highest_seen
        # else add our range
        else:
            count += end - start + 1
        if end > highest_seen:
            highest_seen = end

    return count


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

    data = reader.raw

    print("Advent of Code 2025 - Day X")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
