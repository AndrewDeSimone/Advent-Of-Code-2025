INPUT_FILE = r'Day2\input.txt'

def is_invalid_id_2(id_value: int) -> bool:
    s = str(id_value)
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def is_invalid_id_n(id_value: int) -> bool:
    s = str(id_value)
    size = len(s)
    for n in range(2, size+1):
        if size % n != 0:
            continue

        chunk_size = size // n
        if all(s[i:i+chunk_size] == s[:chunk_size] for i in range(0, size, chunk_size)):
            return True 
    
    return False
        

def sum_invalid_ids(filepath: str, is_invalid_id: callable) -> int:
    total = 0

    with open(filepath, 'r') as file:
        intervals = file.readline().strip().split(',')

    for interval in intervals:
        start_str, end_str = interval.split('-')
        start, end = int(start_str), int(end_str)

        for value in range(start, end + 1):
            if is_invalid_id(value):
                total += value

    return total

if __name__ == '__main__':
    print(sum_invalid_ids(INPUT_FILE, is_invalid_id_2))
    print(sum_invalid_ids(INPUT_FILE, is_invalid_id_n))