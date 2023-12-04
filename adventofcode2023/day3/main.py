# Part 1

def read_file(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def is_symbol(char):
    return char not in "0123456789."

def is_adjacent_to_symbol(grid, x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and is_symbol(grid[nx][ny]):
            return True
    return False

def extract_numbers(grid):
    numbers = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y].isdigit():
                if y == 0 or not grid[x][y-1].isdigit():
                    number = ''
                    while y < len(grid[x]) and grid[x][y].isdigit():
                        number += grid[x][y]
                        y += 1
                    numbers.append((int(number), x, y - len(number)))
    return numbers

def sum_part_numbers(grid):
    total = 0
    numbers = extract_numbers(grid)
    for number, x, start_y in numbers:
        for y in range(start_y, start_y + len(str(number))):
            if is_adjacent_to_symbol(grid, x, y):
                total += number
                break
    return total

# Main function to read the file and calculate the sum
def main(filename):
    grid = read_file(filename)
    return sum_part_numbers(grid)

# Example usage
sum_of_parts = main("input.txt")
print(sum_of_parts)


# PART 2
def find_gears(grid):
    gears = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '*':
                gears.append((x, y))
    return gears

def calculate_gear_ratio(grid, gear_pos, numbers):
    x, y = gear_pos
    adjacent_numbers = []
    for number, nx, start_y in numbers:
        for ny in range(start_y, start_y + len(str(number))):
            if abs(nx - x) <= 1 and abs(ny - y) <= 1:
                adjacent_numbers.append(number)
                break
        if len(adjacent_numbers) == 2:
            break
    return adjacent_numbers[0] * adjacent_numbers[1] if len(adjacent_numbers) == 2 else 0

def sum_gear_ratios(grid, numbers):
    total_ratio = 0
    gears = find_gears(grid)
    for gear in gears:
        gear_ratio = calculate_gear_ratio(grid, gear, numbers)
        if gear_ratio != 0:
            total_ratio += gear_ratio
    return total_ratio

# You can use this function along with the existing main function
def main_gear_ratio(filename):
    grid = read_file(filename)
    numbers = extract_numbers(grid)
    return sum_gear_ratios(grid, numbers)

total_gear_ratio = main_gear_ratio("input.txt")
print(total_gear_ratio)
