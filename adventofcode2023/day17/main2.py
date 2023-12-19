import heapq

def read_input(file_path):
    with open(file_path, 'r') as file:
        grid = [[int(char) for char in line.strip()] for line in file]
    return grid

def get_neighbors(pos, direction, straight_moves, grid, end):
    x, y = pos
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    grid_width = len(grid[0])
    grid_height = len(grid)

    for i, d in enumerate(directions):
        if direction is not None and (i + 2) % 4 == direction:
            continue  # Skip the reverse direction

        nx, ny = x + d[0], y + d[1]
        if not (0 <= nx < grid_height and 0 <= ny < grid_width):
            continue  # Skip moves that go off the grid

        if (nx, ny) == end and straight_moves < 3:
            continue  # Skip moves to the final square that don't meet the minimum movement requirement

        if direction is None:
            neighbors.append(((nx, ny), i))  # Can move in any direction initially
        elif direction == i:
            if straight_moves < 10:
                neighbors.append(((nx, ny), i))  # Continue in the same direction
        elif straight_moves >= 4:
            neighbors.append(((nx, ny), i))  # Can turn if it has moved at least four blocks

    return neighbors

def dijkstra(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    heap = [(0, start, None, 0, [])]  # (heat loss, position, direction, straight moves, path)
    visited = set()
    high_cost = 1_000_000

    while heap:
        heat_loss, pos, direction, straight_moves, path = heapq.heappop(heap)
        visited_key = (pos, direction, straight_moves)

        if visited_key in visited:
            continue
        visited.add(visited_key)

        current_path = path + [pos]

        if pos == end:
            return heat_loss, current_path

        for neighbor, new_direction in get_neighbors(pos, direction, straight_moves, grid, end):
            new_straight_moves = straight_moves + 1 if new_direction == direction else 1

            # Check if moving to this neighbor would violate the minimum movement rule at the final square
            if neighbor == end and new_straight_moves < 4:
                heapq.heappush(heap, (high_cost, neighbor, new_direction, new_straight_moves, current_path))
            else:
                heapq.heappush(heap, (heat_loss + grid[neighbor[0]][neighbor[1]], neighbor, new_direction, new_straight_moves, current_path))

    return float('inf'), []


def main():
    grid = read_input("input.txt")
    heat_loss, path = dijkstra(grid)
    print(f"Minimum heat loss: {heat_loss}")
    print("Path:", path)

if __name__ == "__main__":
    main()

# 899 is too low
# ffs it was 900