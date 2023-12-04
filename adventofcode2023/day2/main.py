# Part 1 

def parse_line(line):
    """
    Parses a line from the input and returns a list of tuples representing the cube counts in each set.
    """
    # Removing 'Game X:' part and splitting the line into sets
    sets = line.split(':')[1].strip().split(';')
    
    # Parsing each set into a dictionary of colors and counts
    game_data = []
    for set in sets:
        set_data = {}
        for cube in set.strip().split(','):
            count, color = cube.strip().split()
            set_data[color] = int(count)
        game_data.append(set_data)
    
    return game_data

def is_game_possible(game_data, cube_limits):
    """
    Checks if a game is possible with the given limits of cubes.
    """
    for set in game_data:
        for color, count in set.items():
            if count > cube_limits[color]:
                return False
    return True

# Cube limits
cube_limits = {'red': 12, 'green': 13, 'blue': 14}

# Read in data from input.txt and analyze each game
with open('input.txt', 'r') as file:
    lines = file.readlines()

possible_games_sum = 0
for line in lines:
    game_id = int(line.split(':')[0].split()[-1])  # Extracting game ID
    game_data = parse_line(line)
    
    if is_game_possible(game_data, cube_limits):
        possible_games_sum += game_id

# Print the sum of IDs of possible games
print(possible_games_sum)

# Part 2

def find_minimum_cubes(game_data):
    """
    Finds the minimum number of cubes of each color required for a game.
    """
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for set in game_data:
        for color, count in set.items():
            min_cubes[color] = max(min_cubes[color], count)
    return min_cubes

def calculate_power(cube_set):
    """
    Calculates the power of a set of cubes, defined as the product of the number of cubes of each color.
    """
    return cube_set['red'] * cube_set['green'] * cube_set['blue']

# Read in data from input.txt and analyze each game
with open('input.txt', 'r') as file:
    lines = file.readlines()

total_power = 0
for line in lines:
    game_data = parse_line(line)
    min_cubes = find_minimum_cubes(game_data)
    total_power += calculate_power(min_cubes)

# Print the total power of all games
print(total_power)