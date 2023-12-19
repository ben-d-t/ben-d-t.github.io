def read_input(file_path):
    with open(file_path, 'r') as file:
        print("Reading input file...")
        return [list(line.strip()) for line in file]

def expand_universe(grid):
    print("Expanding the universe...")
    # Identify rows and columns with no galaxies in the original grid
    original_row_count = len(grid)
    original_col_count = len(grid[0])

    empty_rows = [i for i in range(original_row_count) if '#' not in grid[i]]
    empty_cols = [j for j in range(original_col_count) if all(grid[i][j] == '.' for i in range(original_row_count))]

    # Double the size of empty rows and columns based on the original grid
    for row in reversed(empty_rows):  # Reverse to maintain index order during insertion
        grid.insert(row, ['.'] * original_col_count)
    for col in reversed(empty_cols):  # Reverse to maintain index order during insertion
        for row in grid:
            row.insert(col, '.')

    print("Expansion completed.")
    return grid

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def assign_galaxies(grid):
    print("Assigning numbers to galaxies...")
    galaxy_positions = {}
    galaxy_number = 1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                grid[i][j] = str(galaxy_number)
                galaxy_positions[galaxy_number] = (i, j)
                galaxy_number += 1
    print(f"Assigned numbers to {len(galaxy_positions)} galaxies.")
    return galaxy_positions, grid

def bfs_shortest_path(grid, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), distance = queue.pop(0)
        if (x, y) == end:
            return distance
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))
    return float('inf')  # if no path found

def main():
    grid = read_input('input.txt')
    grid = expand_universe(grid)
    galaxies, grid_with_numbers = assign_galaxies(grid)

    #print("Map after numbering galaxies:")
    #print_grid(grid_with_numbers)

    total_path_length = 0
    galaxy_count = len(galaxies)
    print(f"Calculating shortest paths between {galaxy_count} galaxies...")

    for i in range(1, galaxy_count):
        for j in range(i + 1, galaxy_count + 1):
            path_length = bfs_shortest_path(grid, galaxies[i], galaxies[j])
            print(f"Processed galaxy pair ({i}, {j}) - Distance: {path_length}")
            total_path_length += path_length

    print("Total sum of shortest paths:", total_path_length)
    #print("Map at the end:")
    #print_grid(grid_with_numbers)

#if __name__ == "__main__":
#    main()

# 9197106 is too high
# 9177603 is correct

# PART TWO

def mark_expansion(grid):
    print("Marking rows and columns for expansion...")
    # Identify rows and columns with no galaxies in the original grid
    original_row_count = len(grid)
    original_col_count = len(grid[0])

    expanded_rows = set([i for i in range(original_row_count) if '#' not in grid[i]])
    expanded_cols = set([j for j in range(original_col_count) if all(grid[i][j] == '.' for i in range(original_row_count))])

    return expanded_rows, expanded_cols

def bfs_shortest_path_with_cost(grid, start, end, expanded_rows, expanded_cols):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), distance = queue.pop(0)
        if (x, y) == end:
            return distance
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                step_cost = 1 if nx not in expanded_rows and ny not in expanded_cols else 1000000
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + step_cost))
    return float('inf')  # if no path found

def main_part_two():
    grid = read_input('input.txt')
    expanded_rows, expanded_cols = mark_expansion(grid)
    galaxies, grid_with_numbers = assign_galaxies(grid)

    total_path_length = 0
    galaxy_count = len(galaxies)
    print(f"Calculating shortest paths between {galaxy_count} galaxies with expanded universe rules...")

    for i in range(1, galaxy_count):
        for j in range(i + 1, galaxy_count + 1):
            path_length = bfs_shortest_path_with_cost(grid, galaxies[i], galaxies[j], expanded_rows, expanded_cols)
            print(f"Processed galaxy pair ({i}, {j}) - Distance: {path_length}")

            total_path_length += path_length

    print("Map at the end:")
    print_grid(grid_with_numbers)

    print("Total sum of shortest paths in the expanded universe:", total_path_length)

if __name__ == "__main__":
    main_part_two()
