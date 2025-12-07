from typing import Set, Tuple, Dict
INPUT_FILE = r'Day7\input.txt'

def parse_input(filepath: str) -> Tuple[Set[complex], Dict[complex, int], int]:
    splitters = set()
    beams = {}
    grid_height = 0
    with open(filepath, 'r') as file:
        for row_idx, row in enumerate(file.readlines()):
            grid_height += 1
            for col_idx, value in enumerate(row):
                if value == 'S':
                    beams[col_idx + row_idx * 1j] = 1
                elif value == '^':
                    splitters.add(col_idx + row_idx * 1j)

    return splitters, beams, grid_height

def move_beams(beams: Dict[complex, int]) -> Dict[complex, int]:
    moved_beams = {}
    for beam in beams:
        moved_beams[beam + 1j] = moved_beams.get(beam + 1j, 0) + beams[beam]
    return moved_beams

def split_beams(beams: Dict[complex, int], splitters: Set[complex]) -> Tuple[Dict[complex, int], int]:
    split_count = 0
    split_beams = {}

    for beam in beams:
        if beam not in splitters:
            split_beams[beam] = split_beams.get(beam, 0) + beams[beam]
            continue
        split_count += 1
        split_beams[beam + 1] = split_beams.get(beam + 1, 0) + beams[beam]
        split_beams[beam - 1] = split_beams.get(beam - 1, 0) + beams[beam]

    return split_beams, split_count

def calculate_total_splits(filepath: str) -> Tuple[int, int]:
    splitters, beams, grid_height = parse_input(filepath)

    split_count = 0
    for i in range(grid_height):
        beams = move_beams(beams)

        beams, iteration_split_count = split_beams(beams, splitters)
        split_count += iteration_split_count
    
    return split_count, sum(beams.values())

if __name__ == '__main__':
    print(calculate_total_splits(INPUT_FILE))