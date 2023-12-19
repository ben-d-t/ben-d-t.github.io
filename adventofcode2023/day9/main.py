def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def extrapolate_next_value(history, is_debug=False):
    sequences = [history]

    # Generate sequences of differences
    while len(set(sequences[-1])) != 1:
        next_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)]
        sequences.append(next_sequence)
        if is_debug:
            print(f"Sequence: {next_sequence}")

    # Backtrack to find next value in the original sequence
    for i in range(len(sequences) - 1, 0, -1):
        next_value = sequences[i-1][-1] + sequences[i][-1]
        sequences[i-1].append(next_value)
        if is_debug:
            print(f"Backtracking - Adding {sequences[i][-1]} to {sequences[i-1][-2]} to get {next_value}")

    return sequences[0][-1]

def main():
    histories = read_input("input.txt")
    sum_extrapolated = 0

    for i, history in enumerate(histories):
        if i < 15:  # Print details for the first 5 histories
            #print(f"\nProcessing history {i+1}: {history}")
            x = extrapolate_next_value(history, is_debug=True)
            #print(f"Extrapolated value for history {i+1}: {x}")
        else:
            x = extrapolate_next_value(history)
        print(x)
        sum_extrapolated += x

    print(f"\nThe sum of the extrapolated values is: {sum_extrapolated}")

if __name__ == "__main__":
    main()


# 1708206327 is too high
# 1708206096

# PART TWO
def extrapolate_previous_value(history):
    sequences = [history]

    # Generate sequences of differences
    while len(set(sequences[-1])) != 1:
        next_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)]
        sequences.append(next_sequence)

    # Backtrack to find previous value in the original sequence
    for i in range(len(sequences) - 1, 0, -1):
        prev_value = sequences[i-1][0] - sequences[i][0]
        sequences[i-1].insert(0, prev_value)

    return sequences[0][0]

def main2():
    histories = read_input("input.txt")
    sum_extrapolated_previous = sum(extrapolate_previous_value(history) for history in histories)
    print(f"The sum of the extrapolated previous values is: {sum_extrapolated_previous}")

if __name__ == "__main__":
    main2()
