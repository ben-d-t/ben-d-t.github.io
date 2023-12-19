def read_input(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def print_array(array):
    for row in array:
        print(''.join(row))
    print()

def tilt(array, direction):
    height, width = len(array), len(array[0])

    if direction == 'north':
        for col in range(width):
            for row in range(height):
                if array[row][col] == 'O':
                    new_row = row
                    while new_row > 0 and array[new_row - 1][col] == '.':
                        new_row -= 1
                    if new_row != row:
                        array[row][col], array[new_row][col] = '.', 'O'

    elif direction == 'south':
        for col in range(width):
            for row in range(height - 1, -1, -1):
                if array[row][col] == 'O':
                    new_row = row
                    while new_row < height - 1 and array[new_row + 1][col] == '.':
                        new_row += 1
                    if new_row != row:
                        array[row][col], array[new_row][col] = '.', 'O'

    elif direction == 'east':
        for row in range(height):
            for col in range(width - 1, -1, -1):
                if array[row][col] == 'O':
                    new_col = col
                    while new_col < width - 1 and array[row][new_col + 1] == '.':
                        new_col += 1
                    if new_col != col:
                        array[row][col], array[row][new_col] = '.', 'O'

    elif direction == 'west':
        for row in range(height):
            for col in range(width):
                if array[row][col] == 'O':
                    new_col = col
                    while new_col > 0 and array[row][new_col - 1] == '.':
                        new_col -= 1
                    if new_col != col:
                        array[row][col], array[row][new_col] = '.', 'O'

    return array



def calculate_load(array, direction):
    load = 0
    height, width = len(array), len(array[0])

    if direction == 'north':
        for row in range(height):
            for col in range(width):
                if array[row][col] == 'O':
                    load += height - row  # Load is based on distance from the south edge

    # Logic for other directions can be added here if needed

    return load

def array_to_str(array):
    return '\n'.join([''.join(row) for row in array])

def tilt_and_calculate_load(filename, cycles):
    array = read_input(filename)
    print("Array before cycles:")
    print_array(array)

    seen_configs = {array_to_str(array): 0}
    directions = ['north', 'west', 'south', 'east']

    for cycle in range(1, cycles + 1):
        for direction in directions:
            array = tilt(array, direction)

        array_str = array_to_str(array)
        if array_str in seen_configs:
            cycle_length = cycle - seen_configs[array_str]
            remaining_cycles = (cycles - cycle) % cycle_length
            for _ in range(remaining_cycles):
                for direction in directions:
                    array = tilt(array, direction)
            break
        else:
            seen_configs[array_str] = cycle

        if cycle % 10000 == 0:  # Print progress every 10000 cycles
            print(f"Completed cycle: {cycle}")

    print("Array after all cycles:")
    print_array(array)

    return calculate_load(array, 'north')
# Example usage
filename = "input.txt"
cycles = 1000000000
# 1,000,000,000
total_load = tilt_and_calculate_load(filename, cycles)
print(f"Total load on the north support beams after {cycles} cycles: {total_load}")
