import math
from typing import Tuple, List

INPUT_FILE = r'Day6\input.txt'

def split_row_by_widths(row: str, widths: str) -> List[str]:
    position = 0
    nums = []
    for width in widths:
        nums.append(row[position: position + width])
        position += width + 1
    return nums


def compute_column_widths(operations: str) -> List[int]:
    widths = [1]
    for char in operations[1:]:
        if char in {'*', '+'}:
            widths[-1] -= 1
            widths.append(1)
        else:
            widths[-1] += 1
    
    return widths


def parse_input(filepath: str) -> Tuple[List[str], List[str]]:
    with open(filepath, 'r') as file:
        rows = [row for row in file.readlines()]
    
    operation_row = rows[-1]
    operations = operation_row.split()
    widths = compute_column_widths(rows[-1])
    
    numbers = [split_row_by_widths(row, widths) for row in rows[:-1]]

    return numbers, operations


def vertical_numbers(number_rows: List[List[str]]) -> List[List[str]]:
   
    result = []
    columns = list(zip(*number_rows))

    for col in columns:
        max_len = max(len(s) for s in col)
        padded = [s.rjust(max_len) for s in col]

        vertical_nums = []
        for i in range(max_len):
           vertical_slice = ''.join(row[i] for row in padded).strip()
           if vertical_slice:
               vertical_nums.append(vertical_slice)
        
        result.append(vertical_nums)
    
    return result


def compute_total(filepath: str, is_part2: bool = False) -> int:
    total = 0
    
    numbers, operations = parse_input(filepath)

    if is_part2:
        numbers = vertical_numbers(numbers)
        for col, op in zip(numbers, operations):
            column_values = [int(value) for value in col]
            if op == '+':
                total += sum(column_values)
            elif op == '*':
                total += math.prod(column_values)
            else:
                raise ValueError(f"Invalid operator {op}")
    else:
        for op_idx, op in enumerate(operations):
            column_values = [int(row[op_idx]) for row in numbers]
            if op == '+':
                total += sum(column_values)
            elif op == '*':
                total += math.prod(column_values)
            else:
                raise ValueError(f'Invalid operator {op}')
    
    return total

if __name__ == '__main__':
    print(compute_total(INPUT_FILE))
    print(compute_total(INPUT_FILE, True))