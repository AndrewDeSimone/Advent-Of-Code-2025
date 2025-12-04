from typing import List, Set
INPUT_FILE = r'Day4\input.txt'

NEIGHBOR_OFFSETS = [
    -1 - 1j, -1 + 0j, -1 + 1j,
     0 - 1j,          0 + 1j,
     1 - 1j,  1 + 0j, 1 + 1j,
]

def parse_input(input: List[str]) -> Set[complex]:
    rolls: Set[complex] = set()
    for row_index, row in enumerate(input):
        for col_index, value in enumerate(row):
            if value == "@":
                rolls.add(row_index + col_index * 1j)
    return rolls

def remove_and_count(rolls: Set[complex]) -> int:
    total = 0
    while True:
        accessible =  [
            roll for roll in rolls
            if sum(1 for offset in NEIGHBOR_OFFSETS if roll + offset in rolls) < 4
        ]
        
        if not accessible:
            return total
        
        total += len(accessible)
        
        for roll in accessible:
            rolls.remove(roll)

def count_only(rolls: Set[complex]) -> int:
    return len(
        [
            roll for roll in rolls
            if sum(1 for offset in NEIGHBOR_OFFSETS if roll + offset in rolls) < 4
        ]
    )

def total_accessible_rolls(filepath: str, count_fn: callable) -> int:
    with open(filepath, "r") as file:
        rolls = parse_input(file.readlines())
    return count_fn(rolls)

if __name__ == "__main__":
    print(total_accessible_rolls(INPUT_FILE, count_only))
    print(total_accessible_rolls(INPUT_FILE, remove_and_count))