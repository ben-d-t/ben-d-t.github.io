def read_input(file_path):
    with open(file_path, 'r') as file:
        return [pattern.split('\n') for pattern in file.read().strip().split('\n\n')]

def is_vertical_mirror_line(pattern, line_idx):
    cols = len(pattern[0])
    # Ensure columns line_idx and line_idx + 1 are identical
    if all(row[line_idx] == row[line_idx + 1] for row in pattern):
        # Check the minimum number of columns on either side
        min_side = min(line_idx, cols - line_idx - 2)
        for i in range(min_side + 1):
            if any(row[line_idx - i] != row[line_idx + 1 + i] for row in pattern):
                return False
        return True
    return False

def is_horizontal_mirror_line(pattern, line_idx):
    rows = len(pattern)
    # Ensure rows line_idx and line_idx + 1 are identical
    if pattern[line_idx] == pattern[line_idx + 1]:
        # Check the minimum number of rows on either side
        min_side = min(line_idx, rows - line_idx - 2)
        for i in range(min_side + 1):
            if pattern[line_idx - i] != pattern[line_idx + 1 + i]:
                return False
        return True
    return False

def find_mirror_line(pattern, skip_idx=None, skip_type=None):
    rows, cols = len(pattern), len(pattern[0])

    # Check each possible vertical mirror line
    for col_idx in range(cols - 1):
        if is_vertical_mirror_line(pattern, col_idx):
            if skip_type == 'vertical' and col_idx + 1 == skip_idx:
                continue  # Skip the original vertical mirror line
            return col_idx + 1, 'vertical'

    # Check each possible horizontal mirror line
    for row_idx in range(rows - 1):
        if is_horizontal_mirror_line(pattern, row_idx):
            if skip_type == 'horizontal' and row_idx + 1 == skip_idx:
                continue  # Skip the original horizontal mirror line
            return row_idx + 1, 'horizontal'

    return None, None


def calculate_score(patterns):
    total_score = 0

    for pattern in patterns:
        mirror_idx, mirror_type = find_mirror_line(pattern)
        print(f"Mirror Line: {mirror_idx}, Type: {mirror_type}")

        if mirror_type == 'vertical':
            score = mirror_idx  # The score is already the number of columns to the left
        elif mirror_type == 'horizontal':
            score = 100 * mirror_idx  # The score is already 100 times the number of rows above
        else:
            score = 0

        print(f"Score for this pattern: {score}")
        total_score += score

    return total_score

def main():
    patterns = read_input('input.txt')
    print("Parsed Patterns:")
    for pattern in patterns:
        print("\n".join(pattern))
        print("---")

    score = calculate_score(patterns)
    print(f"Total Score: {score}")

if __name__ == "__main__":
    main()
