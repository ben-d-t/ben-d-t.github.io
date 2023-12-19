import heapq

def read_input(file_path):
    with open(file_path, 'r') as file:
        grid = [[int(char) for char in line.strip()] for line in file]
    return grid

def get_neighbors(pos, direction, straight_moves, grid):
    x, y = pos
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for i, d in enumerate(directions):
        if direction is not None and (i + 2) % 4 == direction:
            continue  # Skip the reverse direction

        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if direction is None or (direction == i and straight_moves < 3) or (direction != i):
                neighbors.append(((nx, ny), i))
    return neighbors

def dijkstra(grid):
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    heap = [(0, start, None, 0, [])]  # (heat loss, position, direction, straight moves, path)
    visited = set()

    while heap:
        heat_loss, pos, direction, straight_moves, path = heapq.heappop(heap)
        visited_key = (pos, direction, straight_moves)

        if visited_key in visited:
            continue
        visited.add(visited_key)

        current_path = path + [pos]

        if pos == end:
            return heat_loss, current_path

        for neighbor, new_direction in get_neighbors(pos, direction, straight_moves, grid):
            new_straight_moves = straight_moves + 1 if new_direction == direction else 1
            heapq.heappush(heap, (heat_loss + grid[neighbor[0]][neighbor[1]], neighbor, new_direction, new_straight_moves, current_path))

    return float('inf'), []

def main():
    grid = read_input("input.txt")
    heat_loss, path = dijkstra(grid)
    print(f"Minimum heat loss: {heat_loss}")
    print("Path:", path)

if __name__ == "__main__":
    main()


# print(f"Pushing: {(new_x, new_y)}, Cost: {new_cost}")
# 826 is too high
# 756 is too low