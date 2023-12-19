import itertools

def count_question_marks(spring_row):
    return spring_row.count('?')

def generate_all_combinations(spring_row):
    question_mark_indices = [i for i, x in enumerate(spring_row) if x == '?']
    for replacement in itertools.product(['#', '.'], repeat=len(question_mark_indices)):
        yield ''.join(spring_row[i] if i not in question_mark_indices else replacement[question_mark_indices.index(i)] for i in range(len(spring_row)))

def is_valid_arrangement(spring_row, group_sizes):
    groups = [list(g) for k, g in itertools.groupby(spring_row, lambda x: x == '#') if k]
    return len(groups) == len(group_sizes) and all(len(group) == size for group, size in zip(groups, group_sizes))

def count_valid_arrangements(spring_row, group_sizes):
    total_arrangements = 0
    for arrangement in generate_all_combinations(spring_row):
        if is_valid_arrangement(arrangement, group_sizes):
            total_arrangements += 1
    return total_arrangements

def main():
    total_count = 0
    with open('test.txt', 'r') as file:
        for line in file:
            spring_row, group_info = line.strip().split(' ')
            group_sizes = list(map(int, group_info.split(',')))

            num_question_marks = count_question_marks(spring_row)
            possible_arrangements = 2 ** num_question_marks

            print(f"Processing row: {spring_row}, Possible arrangements: {possible_arrangements}")
            valid_arrangements = count_valid_arrangements(spring_row, group_sizes)
            print(f"Row: {spring_row} {group_info} - {valid_arrangements} valid arrangements")

            total_count += valid_arrangements

    print(f"Total valid arrangements across all rows: {total_count}")

if __name__ == "__main__":
    main()

# 7025 correct