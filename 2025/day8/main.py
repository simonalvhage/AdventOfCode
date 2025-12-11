from pathlib import Path
import math


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
    pairs = []
    for first_neighbour in data:
        for second_neighbour in data:
            if first_neighbour < second_neighbour:
                dist = math.dist((int(first_neighbour.split(",")[0]), int(first_neighbour.split(",")[1]),
                                  int(first_neighbour.split(",")[2])),
                                 (int(second_neighbour.split(",")[0]), int(second_neighbour.split(",")[1]),
                                  int(second_neighbour.split(",")[2])))
                pairs.append((dist, first_neighbour, second_neighbour))
    pairs.sort()

    circuits = [{first_neighbour} for first_neighbour in data]

    for dist, first_neighbour, second_neighbour in pairs[:1000]:
        for circuit in circuits:
            if first_neighbour in circuit:
                circuit1 = circuit
            if second_neighbour in circuit:
                circuit2 = circuit

        if circuit1 is not circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

    sizes = []
    for c in circuits:
        sizes.append(len(c))
    sizes.sort(reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


def part2(data) -> int | None:
    pairs = []
    for first_neighbour in data:
        for second_neighbour in data:
            if first_neighbour < second_neighbour:
                dist = math.dist((int(first_neighbour.split(",")[0]), int(first_neighbour.split(",")[1]),
                                  int(first_neighbour.split(",")[2])),
                                 (int(second_neighbour.split(",")[0]), int(second_neighbour.split(",")[1]),
                                  int(second_neighbour.split(",")[2])))
                pairs.append((dist, first_neighbour, second_neighbour))
    pairs.sort()

    circuits = [{first_neighbour} for first_neighbour in data]

    for dist, first_neighbour, second_neighbour in pairs:
        for circuit in circuits:
            if first_neighbour in circuit:
                circuit1 = circuit
            if second_neighbour in circuit:
                circuit2 = circuit

        if circuit1 is not circuit2:
            circuit1.update(circuit2)
            circuits.remove(circuit2)

            if len(circuits) == 1:
                x1 = int(first_neighbour.split(",")[0])
                x2 = int(second_neighbour.split(",")[0])
                return x1 * x2


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
