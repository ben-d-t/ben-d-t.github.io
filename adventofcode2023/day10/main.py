def read_input(file_path):
    with open(file_path, 'r') as file:
        original_grid = [list(line.strip()) for line in file]

    # Adding a perimeter of '.' around the original grid
    width = len(original_grid[0]) + 2
    extended_grid = [['.' for _ in range(width)]]
    for row in original_grid:
        extended_grid.append(['.'] + row + ['.'])
    extended_grid.append(['.' for _ in range(width)])

    return extended_grid


def find_start(grid):
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 'S':
                return x, y
    return None, None

def is_valid_move(grid, x, y, prev_x, prev_y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return False
    if x == prev_x and y == prev_y:
        return False
    if grid[y][x] == '.':
        return False
    return True

def is_connected(grid, x, y, direction):
    pipe = grid[y][x]
    if pipe == '|':
        return direction in ['north', 'south']
    elif pipe == '-':
        return direction in ['east', 'west']
    elif pipe == 'L':
        return direction in ['north', 'east']
    elif pipe == 'J':
        return direction in ['north', 'west']
    elif pipe == '7':
        return direction in ['south', 'west']
    elif pipe == 'F':
        return direction in ['south', 'east']
    elif pipe == 'S':
        return True  # 'S' can connect in any direction as it's a starting point
    return False

def get_next_move(grid, x, y, prev_x, prev_y):
    directions = {
        'north': (0, -1),
        'south': (0, 1),
        'east': (1, 0),
        'west': (-1, 0)
    }

    for dir, (dx, dy) in directions.items():
        next_x, next_y = x + dx, y + dy
        if next_x == prev_x and next_y == prev_y:
            continue  # Avoid backtracking

        if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
            if is_connected(grid, x, y, dir) and is_connected(grid, next_x, next_y, opposite_direction(dir)):
                return next_x, next_y

    return None, None

def opposite_direction(direction):
    opposites = {
        'north': 'south',
        'south': 'north',
        'east': 'west',
        'west': 'east'
    }
    return opposites[direction]

# Other functions (read_input, find_start, traverse_loop, main) remain the same.


def traverse_loop(grid, start_x, start_y):
    x, y = start_x, start_y
    prev_x, prev_y = -1, -1
    steps = 0

    while True:
        next_x, next_y = get_next_move(grid, x, y, prev_x, prev_y)
        if next_x is None or next_y is None:
            break  # No valid moves found

        prev_x, prev_y = x, y
        x, y = next_x, next_y
        steps += 1

        if x == start_x and y == start_y:
            break  # Loop completed

    return steps // 2


# PART TWO
def is_accessible_for_flood_fill(grid, x, y, visited, loop_tiles):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    if visited[y][x]:
        return False
    # Consider all tiles as accessible except those that are part of the main loop
    return (x, y) not in loop_tiles

def flood_fill(grid, x, y, visited, loop_tiles):
    if not is_accessible_for_flood_fill(grid, x, y, visited, loop_tiles):
        return

    visited[y][x] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        flood_fill(grid, next_x, next_y, visited, loop_tiles)

def traverse_and_mark_loop(grid, start_x, start_y):
    x, y = start_x, start_y
    prev_x, prev_y = -1, -1
    loop_tiles = set()  # To keep track of loop tiles

    while True:
        loop_tiles.add((x, y))  # Mark the current tile as part of the loop
        next_x, next_y = get_next_move(grid, x, y, prev_x, prev_y)
        if next_x is None or next_y is None:
            break

        prev_x, prev_y = x, y
        x, y = next_x, next_y

        if x == start_x and y == start_y:
            break  # Loop completed

    return loop_tiles

def print_grid_with_markers(grid, visited, loop_tiles):
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if (x, y) in loop_tiles:
                print('X', end='')
            elif visited[y][x]:
                print('O', end='')
            else:
                print('I', end='')
        print()

def count_enclosed_tiles(grid, start_x, start_y):
    visited = [[False for _ in row] for row in grid]
    loop_tiles = traverse_and_mark_loop(grid, start_x, start_y)
    flood_fill(grid, 0, 0, visited, loop_tiles)  # Start from top-left corner

    enclosed_count = 0
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if not visited[y][x] and (x, y) not in loop_tiles:
                enclosed_count += 1

    print_grid_with_markers(grid, visited, loop_tiles)
    return enclosed_count

# Other functions (read_input, find_start, traverse_loop, main) remain the same.

def main():
    grid = read_input("test.txt")
    start_x, start_y = find_start(grid)
    if start_x is not None and start_y is not None:
        farthest_point_distance = traverse_loop(grid, start_x, start_y)
        print("Farthest point from the start:", farthest_point_distance)
    else:
        print("Starting position not found.")
    # Include this function in your existing code and call it after you've found the loop
    enclosed_tiles = count_enclosed_tiles(grid, start_x, start_y)
    print("Number of tiles enclosed by the loop:", enclosed_tiles)


if __name__ == "__main__":
    main()

# 19600 is too high
# 19058 is too high
# 11961 is too high 