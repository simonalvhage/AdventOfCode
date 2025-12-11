from pathlib import Path
from scipy.optimize import milp, LinearConstraint, Bounds

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
    result = 0
    for line in data:
        min_presses = 9999
        test_indicator = []
        indicator = line.split(" ")[0]
        schematics = line.split(" ")[1:-1]
        j_requirements = line.split(" ")[-1]
        list_indicator = list(indicator)[1:-1]
        list_schematics = [[int(item) for item in list(s)[1:-1] if item != ","] for s in schematics]

        for mask in range(2 ** len(list_schematics)):
            test_indicator = ['.'] * len(list_indicator)
            presses = 0

            for button in range(len(list_schematics)):
                if mask & (1 << button):
                    presses += 1
                    for light_idx in list_schematics[button]:
                        if test_indicator[light_idx] == '.':
                            test_indicator[light_idx] = '#'
                        else:
                            test_indicator[light_idx] = '.'

            if test_indicator == list_indicator:
                if presses < min_presses:
                    min_presses = presses
        result += min_presses
    return result


def part2(data) -> int:
    result = 0
    for line in data:
        schematics = line.split(" ")[1:-1]
        j_requirements = line.split(" ")[-1]

        # Fix: använd split för båda
        list_schematics = [[int(x) for x in s[1:-1].split(",")] for s in schematics]
        list_j_requirements = [int(x) for x in j_requirements[1:-1].split(",")]

        equation = [[0] * len(list_schematics) for req in range(len(list_j_requirements))]
        for i, row in enumerate(equation):
            for col in range(len(list_schematics)):
                if i in list_schematics[col]:
                    row[col] = 1

        c = [1] * len(list_schematics)
        #Defines the terms of the milp equation solver, like lb <= A @ x <= ub (kinda :P)
        constraints = LinearConstraint(equation, list_j_requirements, list_j_requirements)
        #Minimize c to the constraints like 1*x0 + 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5
        res = milp(c, constraints=constraints, integrality=c)
        result += int(res.fun)

    return result


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
