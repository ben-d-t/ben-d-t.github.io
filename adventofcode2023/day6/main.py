def calculate_ways_to_win(time, record_distance):
    ways_to_win = 0
    for button_hold_time in range(time):
        travel_time = time - button_hold_time
        distance = button_hold_time * travel_time
        if distance > record_distance:
            ways_to_win += 1
    return ways_to_win

def solve_puzzle_part_one(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    times = [int(time) for time in lines[0].split()[1:]]  # Skip the first word "Time:"
    distances = [int(distance) for distance in lines[1].split()[1:]]  # Skip the first word "Distance:"

    total_ways = 1
    for time, distance in zip(times, distances):
        ways = calculate_ways_to_win(time, distance)
        total_ways *= ways

    return total_ways

def solve_puzzle_part_two(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    time = int(''.join(lines[0].split()[1:]))  # Concatenate and convert to integer
    distance = int(''.join(lines[1].split()[1:]))  # Concatenate and convert to integer

    return calculate_ways_to_win(time, distance)

# Example usage
part_one_result = solve_puzzle_part_one("input.txt")
part_two_result = solve_puzzle_part_two("input.txt")
print("Total ways to win in Part One:", part_one_result)
print("Total ways to win in Part Two:", part_two_result)
