def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    instructions = [line.strip().split() for line in lines]
    return [(instr[0], int(instr[1]), instr[2]) for instr in instructions]

def write_grid_to_file(grid, file_name):
    with open(file_name, 'w') as file:
        for row in grid:
            file.write(''.join(row) + '\n')

def construct_dig_site(instructions):
    grid = {}
    x = y = 0

    # Apply instructions
    for direction, distance, _ in instructions:
        for _ in range(distance):
            grid[(x, y)] = '#'
            if direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1

    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())

    # Create a grid representation
    grid_representation = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for (x, y), value in grid.items():
        grid_representation[y - min_y][x - min_x] = value

    return grid_representation

def fill_dig_site(grid):
    queue = []

    # Find a starting point for fill
    found = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                # Move one square right and one square down from the first "#"
                start_x = min(x + 1, len(grid[0]) - 1)
                start_y = min(y + 1, len(grid) - 1)
                if grid[start_y][start_x] == '.':
                    queue.append((start_x, start_y))
                    found = True
                    break
        if found:
            break

    # Fill using BFS
    while queue:
        x, y = queue.pop(0)
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == '.':
            grid[y][x] = '#'
            queue.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])


def count_filled_area(grid):
    return sum(row.count('#') for row in grid)

# Main execution
input_file = 'input.txt'  # Update with the path of your input file
instructions = read_input(input_file)
dig_site = construct_dig_site(instructions)
filled_site_output_file = 'filled_dig_site.txt'

fill_dig_site(dig_site)
filled_area = count_filled_area(dig_site)
write_grid_to_file(dig_site, filled_site_output_file)
print(f"\nFilled Dig Site written to {filled_site_output_file}")
print(f"Total Area: {filled_area} cubic meters")


# 8048 too low