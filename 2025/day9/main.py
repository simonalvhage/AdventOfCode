from pathlib import Path
from shapely.geometry import Polygon, box


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

def get_area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x2 - x1)+1) * (abs(y2 - y1)+1)


def part1(data) -> int | None:
    red_points = []
    for line in data:
        parts = line.strip().split(",")
        x = int(parts[0])
        y = int(parts[1])
        red_points.append((x, y))

    max_area = 0
    for i in range(len(red_points)):
        for j in range(i + 1, len(red_points)):
            x1, y1 = red_points[i]
            x2, y2 = red_points[j]
            area = get_area(x1, y1, x2, y2)
            if area > max_area:
                max_area = area
    return max_area


def part2(data) -> int:
    red_points = []
    for line in data:
        parts = line.strip().split(",")
        x = int(parts[0])
        y = int(parts[1])
        red_points.append((x, y))

    polygon = Polygon(red_points)
    max_area = 0
    for i in range(len(red_points)):
        for j in range(i + 1, len(red_points)):
            x1, y1 = red_points[i]
            x2, y2 = red_points[j]
            rect = box(x1, y1, x2, y2)

            if polygon.contains(rect):
                area = get_area(x1, y1, x2, y2)
                if area > max_area:
                    max_area = area
    return max_area


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

    data = reader.lines()

    print("Advent of Code 2025 - Day X")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
