def read_and_parse_input(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


def simulate_laser_path(grid):
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
    total_energized = process_beam(0, 0, 'right', path_set)

    return energized

def count_energized_tiles(energized_grid):
    return sum(sum(row) for row in energized_grid)

def print_grid(grid, energized):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print('#' if energized[i][j] else grid[i][j], end='')
        print()

# The path to your input file
file_path = "input.txt"
grid = read_and_parse_input(file_path)

print("Original grid:")
print_grid(grid, [[False]*len(row) for row in grid])

energized_grid = simulate_laser_path(grid)

print("\nEnergized grid:")
print_grid(grid, energized_grid)

result = count_energized_tiles(energized_grid)
print(f"\nNumber of energized tiles: {result}")

# 8901