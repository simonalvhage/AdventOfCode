import sys
sys.path.append("..")
from aoc_helper import InputReader
from shapely.geometry import Polygon, box

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
    reader = InputReader("input.txt")
    data = reader.lines()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
