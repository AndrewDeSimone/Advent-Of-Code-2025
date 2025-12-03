from typing import List
INPUT_FILE = r'Day3\input.txt'

def max_joltage_from_bank(remaining: List[str], count: int) -> str:
    if count == 1:
        return max(remaining)
    chosen = max(remaining[:-count+1])
    next_index = remaining.index(chosen)+1
    return chosen + max_joltage_from_bank(remaining[next_index:], count-1)

def total_joltage(filepath: str, count: int) -> int:
    total = 0

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            total += int(max_joltage_from_bank(list(line), count))
    
    return total

if __name__ == '__main__':
    print(total_joltage(INPUT_FILE, 2))
    print(total_joltage(INPUT_FILE, 12))