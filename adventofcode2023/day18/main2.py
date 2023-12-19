def hex_to_instruction(hex_code):
    # Remove '#' and then split into distance and direction parts
    hex_code = hex_code.replace('#', '')
    distance = int(hex_code[:5], 16)  # Convert first five characters to decimal
    direction = int(hex_code[5], 16)  # Convert the sixth character to decimal
    direction_mapping = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
    print(f"{direction_mapping[direction]} - {distance}")
    return direction_mapping[direction], distance

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Extract the hexadecimal code from the part within parentheses
    hex_codes = [line.strip().split()[-1][1:-1] for line in lines]
    return [hex_to_instruction(hex_code) for hex_code in hex_codes]

def shoelace_formula(coordinates):
    n = len(coordinates)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    return abs(area) / 2

def shoelace_formula_with_correction(coordinates):
    area = shoelace_formula(coordinates)
    boundary_points = 1  # Starting from 1 due to the initial hole

    for i in range(len(coordinates) - 1):
        dx = abs(coordinates[i+1][0] - coordinates[i][0])
        dy = abs(coordinates[i+1][1] - coordinates[i][1])
        # Add the length of the segment plus 1 for the starting/ending square
        boundary_points += dx + dy + 1

    # Adjust for the overcounting at each corner (shared by two segments)
    corner_count = len(coordinates) - 1
    boundary_points -= corner_count

    # Applying Pick's theorem
    return area + (boundary_points / 2) - 1



def construct_boundary_coordinates(instructions):
    x = y = 0
    coordinates = [(x, y)]

    for direction, distance in instructions:
        if direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'R':
            x += distance
        coordinates.append((x, y))

    return coordinates


def count_boundary_cells(coordinates):
    count = 0
    for i in range(len(coordinates) - 1):
        dx = abs(coordinates[i+1][0] - coordinates[i][0])
        dy = abs(coordinates[i+1][1] - coordinates[i][1])
        count += dx + dy  # Sum of dx and dy gives the total cells along the boundary
    return count

# Main execution
# Main execution
input_file = 'input.txt'  # Update with the path of your input file
instructions = read_input(input_file)
boundary_coordinates = construct_boundary_coordinates(instructions)

adjusted_area = shoelace_formula_with_correction(boundary_coordinates)
print(f"Total Area: {adjusted_area} cubic meters")




# 1,407,374,123,584
# 952,408,144,115
# 1.5 off? 
# AH that worked