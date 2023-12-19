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
                continue  # Skip only the original vertical line
            return col_idx + 1, 'vertical'

    # Check each possible horizontal mirror line
    for row_idx in range(rows - 1):
        if is_horizontal_mirror_line(pattern, row_idx):
            if skip_type == 'horizontal' and row_idx + 1 == skip_idx:
                continue  # Skip only the original horizontal line
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

def fix_smudge_and_find_new_reflection_line(pattern, original_mirror_idx, original_mirror_type):
    rows, cols = len(pattern), len(pattern[0])

    for r in range(rows):
        for c in range(cols):
            # Copy the pattern and switch the character at (r, c)
            new_pattern = [list(row) for row in pattern]
            new_pattern[r][c] = '.' if pattern[r][c] == '#' else '#'
            print(f"Testing smudge fix at ({r}, {c})")

            # Check for a new reflection line, skipping the original line
            new_mirror_idx, new_mirror_type = find_mirror_line([''.join(row) for row in new_pattern],
                                                              skip_idx=original_mirror_idx,
                                                              skip_type=original_mirror_type)
            print(f"Found new line: {new_mirror_idx}, Type: {new_mirror_type}")

            # If a new reflection line is found and it's different from the original, return it
            if new_mirror_idx is not None and new_mirror_type and \
               not (new_mirror_idx == original_mirror_idx and new_mirror_type == original_mirror_type):
                return new_mirror_idx, new_mirror_type, [''.join(row) for row in new_pattern]

    return None, None, pattern  # Return the original pattern if no new line is found

# Rest of the script remains the same

def calculate_score_with_smudge_fix(patterns):
    total_score = 0

    for pattern in patterns:
        # Find the original reflection line
        original_mirror_idx, original_mirror_type = find_mirror_line(pattern)
        print(f"Original Mirror Line: {original_mirror_idx}, Type: {original_mirror_type}")

        # Fix smudge and find new reflection line
        result = fix_smudge_and_find_new_reflection_line(pattern, original_mirror_idx, original_mirror_type)

        if result is None:
            raise ValueError("No valid new reflection line found after fixing smudge")

        new_mirror_idx, new_mirror_type, new_pattern = result
        print(f"New Mirror Line: {new_mirror_idx}, Type: {new_mirror_type}")
        print("\n".join(new_pattern))  # Print the pattern after fixing the smudge
        print("---")

        # Calculate score for the new reflection line
        if new_mirror_type == 'vertical':
            score = new_mirror_idx
        elif new_mirror_type == 'horizontal':
            score = 100 * new_mirror_idx
        else:
            score = 0

        print(f"Score for this pattern with smudge fix: {score}")
        total_score += score

    return total_score


def main():
    patterns = read_input('input.txt')
    print("Parsed Patterns:")
    for pattern in patterns:
        print("\n".join(pattern))
        print("---")

    score = calculate_score_with_smudge_fix(patterns)
    print(f"Total Score with Smudge Fix: {score}")

if __name__ == "__main__":
    main()

# 35915 is right