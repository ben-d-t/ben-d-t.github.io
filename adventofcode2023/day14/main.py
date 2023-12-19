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

def tilt_and_calculate_load(filename, direction):
    array = read_input(filename)
    print("Array before tilting:")
    print_array(array)

    tilted_array = tilt(array, direction)
    print("Array after tilting:")
    print_array(tilted_array)

    return calculate_load(tilted_array, direction)

# Example usage
filename = "input.txt"
direction = 'north'
total_load = tilt_and_calculate_load(filename, direction)
print(f"Total load on the north support beams: {total_load}")



# 100843 is too low
# 101258 is too low