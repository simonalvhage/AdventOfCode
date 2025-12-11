from pathlib import Path
import networkx as nx

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
    graph = nx.DiGraph()

    for line in data:
        device, outputs = line.split(':')
        for output in outputs.strip().split():
            graph.add_edge(device.strip(), output)
    #solves all paths
    paths = list(nx.all_simple_paths(graph, "you", "out"))
    return len(paths)


def part2(data) -> int | None:
    graph = nx.DiGraph()

    for line in data:
        device, outputs = line.split(':')
        for output in outputs.strip().split():
            graph.add_edge(device.strip(), output)

    seen = {}
    for n in graph.nodes():
        #Tracking of each combination: [seen none, seen dac, seen fft, seen both]
        seen[n] = [0, 0, 0, 0]
    seen["svr"][0] = 1

    #Count paths through graph, tracking if we've passed dac and fft
    for node in nx.topological_sort(graph):
        for neighbor in graph.successors(node):
            if neighbor == "dac":
                seen[neighbor][1] += seen[node][0] + seen[node][1]
                seen[neighbor][3] += seen[node][2] + seen[node][3]
            elif neighbor == "fft":
                seen[neighbor][2] += seen[node][0] + seen[node][2]
                seen[neighbor][3] += seen[node][1] + seen[node][3]
            else:
                for i in range(4):
                    seen[neighbor][i] += seen[node][i]

    #How many seen both dac and fft and passed out
    return seen["out"][3]


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
