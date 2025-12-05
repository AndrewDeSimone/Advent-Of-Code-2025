from typing import Set, List, Tuple

INPUT_FILE = r'Day5\input.txt'

def parse_input(filepath: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    with open(filepath, 'r') as file:
        raw_ranges, raw_ids = file.read().strip().split('\n\n')
    
    parsed_ids = [int(id_) for id_ in raw_ids.splitlines() if id_]

    parsed_ranges = []
    for line in raw_ranges.split('\n'):
        front, back = line.split('-')
        parsed_ranges.append((int(front), int(back)))
    
    return parsed_ranges, parsed_ids

def is_id_fresh(id_: int, ranges: List[Tuple[int, int]]) -> bool:
    return any(start <= id_ <= end for start, end in ranges)

def count_fresh_ingredients(filepath: str) -> int:
    ranges, ids = parse_input(filepath)

    return sum(1 for id_ in ids if is_id_fresh(id_, ranges))

def merge_ranges(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    sorted_ranges = sorted(ranges, key = lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            merged_ranges.append((start, end))
    
    return merged_ranges

def count_possible_fresh_ingredients(filepath: str) -> int:
    ranges, _ = parse_input(filepath)
    merged_ranges = merge_ranges(ranges)

    return sum(end - start + 1 for start, end in merged_ranges)

if __name__ == '__main__':
    print(count_fresh_ingredients(INPUT_FILE))
    print(count_possible_fresh_ingredients(INPUT_FILE))