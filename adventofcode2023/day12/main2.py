import itertools

def unfold_row(spring_row, group_sizes):
    unfolded_row = (spring_row + '?') * 5
    unfolded_row = unfolded_row[:-1]  # Remove the last extra '?'
    unfolded_group_sizes = group_sizes * 5
    return unfolded_row, unfolded_group_sizes


def count_question_marks(spring_row):
    return spring_row.count('?')

def generate_all_combinations(spring_row):
    question_mark_indices = [i for i, x in enumerate(spring_row) if x == '?']
    for replacement in itertools.product(['#', '.'], repeat=len(question_mark_indices)):
        yield ''.join(spring_row[i] if i not in question_mark_indices else replacement[question_mark_indices.index(i)] for i in range(len(spring_row)))

def is_valid_arrangement(spring_row, group_sizes):
    groups = [list(g) for k, g in itertools.groupby(spring_row, lambda x: x == '#') if k]
    return len(groups) == len(group_sizes) and all(len(group) == size for group, size in zip(groups, group_sizes))

memo_cache = {}

def explore_arrangement(spring_row, group_sizes, index=0, memo={}):
    # Memoization check
    key = (spring_row, index)
    if key in memo:
        return memo[key]

    if index >= len(spring_row):
        if is_valid_arrangement(spring_row, group_sizes):
            return 1
        else:
            return 0

    total_arrangements = 0
    if spring_row[index] == '?':
        # Try replacing '?' with '#' and '.'
        for replacement in ['#', '.']:
            total_arrangements += explore_arrangement(spring_row[:index] + replacement + spring_row[index+1:], group_sizes, index+1, memo)
    else:
        total_arrangements += explore_arrangement(spring_row, group_sizes, index+1, memo)

    memo[key] = total_arrangements
    return total_arrangements

def count_valid_arrangements(spring_row, group_sizes):
    return explore_arrangement(spring_row, group_sizes, 0, {})


def main():
    total_count = 0
    with open('test.txt', 'r') as file:
        for line in file:
            spring_row, group_info = line.strip().split(' ')
            group_sizes = list(map(int, group_info.split(',')))

            unfolded_spring_row, unfolded_group_sizes = unfold_row(spring_row, group_sizes)

            num_question_marks = count_question_marks(unfolded_spring_row)
            possible_arrangements = 2 ** num_question_marks

            print(f"Processing unfolded row: {unfolded_spring_row}, Possible arrangements: {possible_arrangements}")
            valid_arrangements = count_valid_arrangements(unfolded_spring_row, unfolded_group_sizes)
            print(f"Unfolded row: {unfolded_spring_row} - {valid_arrangements} valid arrangements")

            total_count += valid_arrangements

    print(f"Total valid arrangements across all unfolded rows: {total_count}")

if __name__ == "__main__":
    main()
