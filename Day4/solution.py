from typing import List, Dict

INPUT_FILE = r"Day4\input.txt"

NEIGHBOR_OFFSETS = [
    -1 - 1j, -1 + 0j, -1 + 1j,
     0 - 1j,          0 + 1j,
     1 - 1j,  1 + 0j, 1 + 1j,
]

RollGrid = Dict[complex, str]


def parse_diagram(lines: List[str]) -> RollGrid:
    grid: RollGrid = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            grid[row + col * 1j] = char
    return grid


def accessible_rolls(grid: RollGrid) -> List[complex]:
    result = []
    for pos, char in grid.items():
        if char != "@":
            continue
        neighbors = sum(1 for offset in NEIGHBOR_OFFSETS if grid.get(pos + offset) == "@")
        if neighbors < 4:
            result.append(pos)
    return result


def solve_part1(filepath: str) -> int:
    with open(filepath) as file:
        grid = parse_diagram(file.readlines())
    return len(accessible_rolls(grid))


def solve_part2(filepath: str) -> int:
    with open(filepath) as file:
        grid = parse_diagram(file.readlines())

    total_removed = 0
    while True:
        rolls = accessible_rolls(grid)
        if not rolls:
            break
        for pos in rolls:
            grid[pos] = "."
            total_removed += 1
    return total_removed


if __name__ == "__main__":
    print(solve_part1(INPUT_FILE))
    print(solve_part2(INPUT_FILE))
