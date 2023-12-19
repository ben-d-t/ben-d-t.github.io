def read_and_parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


def simulate_laser_path_from_start(grid, start_x, start_y, start_direction):
    def reflect(direction, mirror):
        return {'right': 'up', 'left': 'down', 'up': 'right', 'down': 'left'}[direction] if mirror == '/' else \
            {'right': 'down', 'left': 'up', 'up': 'left', 'down': 'right'}[direction]

    def next_position(x, y, direction):
        deltas = {'right': (0, 1), 'left': (0, -1), 'up': (-1, 0), 'down': (1, 0)}
        return x + deltas[direction][0], y + deltas[direction][1]

    def process_beam(x, y, direction, path_set):
        energized_count = 0
        while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if (x, y, direction) in path_set:
                break  # Path already processed, avoid infinite recursion

            path_set.add((x, y, direction))
            if not energized[x][y]:
                energized[x][y] = True
                energized_count += 1

            cell = grid[x][y]

            if cell in ['/', '\\']:
                direction = reflect(direction, cell)

            elif (cell == '|' and direction in ['left', 'right']) or (cell == '-' and direction in ['up', 'down']):
                # Beam hits the flat side of a splitter
                energized_count += process_beam(x, y, 'up' if direction in ['left', 'right'] else 'left', path_set)
                energized_count += process_beam(x, y, 'down' if direction in ['left', 'right'] else 'right', path_set)
                break

            x, y = next_position(x, y, direction)

        return energized_count

    energized = [[False for _ in row] for row in grid]
    path_set = set()
    process_beam(start_x, start_y, start_direction, path_set)

    return energized

def count_energized_tiles(energized_grid):
    return sum(sum(row) for row in energized_grid)

def print_grid(grid, energized):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print('#' if energized[i][j] else grid[i][j], end='')
        print()


def find_max_energization_configuration(grid):
    max_energized = 0
    rows, cols = len(grid), len(grid[0])
    edge_directions = {
        (0, 0): ['right', 'down'],  # Top-left corner
        (0, cols - 1): ['left', 'down'],  # Top-right corner
        (rows - 1, 0): ['right', 'up'],  # Bottom-left corner
        (rows - 1, cols - 1): ['left', 'up']  # Bottom-right corner
    }

    # Iterate over all edge tiles
    for i in range(rows):
        for j in range(cols):
            directions = []
            if i == 0 or i == rows - 1:  # Top or bottom row
                directions.append('down' if i == 0 else 'up')
            if j == 0 or j == cols - 1:  # Left or right column
                directions.append('right' if j == 0 else 'left')
            if (i, j) in edge_directions:  # Corners
                directions = edge_directions[(i, j)]

            for direction in directions:
                energized = simulate_laser_path_from_start(grid, i, j, direction)
                energized_count = sum(sum(row) for row in energized)
                max_energized = max(max_energized, energized_count)

    return max_energized

# Read input and find configuration
grid = read_and_parse_input("input.txt")
max_tiles_energized = find_max_energization_configuration(grid)
print(f"Maximum number of tiles energized: {max_tiles_energized}")

# 9041 too low