INPUT_FILE = r'Day1\input.txt'
DIAL_SIZE = 100
START_POSITION = 50

def parse_instruction(line: str) -> tuple[str, int]:
    line = line.strip()
    return line[0], int(line[1:])

def apply_rotation(position: int, direction: str, distance: int) -> int:
    if direction == 'L':
        return (position - distance) % DIAL_SIZE
    elif direction == 'R':
        return (position + distance) % DIAL_SIZE
    else:
        raise ValueError(f'Invalid direction: {direction}')

def simulate_rotations(filepath: str, count_clicks_fn: callable) -> int:
    position = START_POSITION
    total_zeros = 0

    with open(filepath, 'r') as file:
        for line in file:
            direction, distance = parse_instruction(line)
            new_position = apply_rotation(position, direction, distance)

            total_zeros += count_clicks_fn(position, new_position, direction, distance)
            position = new_position

    return total_zeros

def count_zeros_end_only(prev_pos, new_pos, direction, distance):
    return 1 if new_pos == 0 else 0

def count_zeros_passed(prev_pos, new_pos, direction, distance):
    signed_distance = distance if direction == 'R' else -distance
    curr = prev_pos + signed_distance

    if signed_distance >= 0:
        return curr // 100 - prev_pos // 100
    else:
        return count_zeros_passed(-prev_pos, -curr, 'R', -signed_distance)


if __name__ == '__main__':
    print(simulate_rotations(INPUT_FILE, count_zeros_end_only))
    print(simulate_rotations(INPUT_FILE, count_zeros_passed))