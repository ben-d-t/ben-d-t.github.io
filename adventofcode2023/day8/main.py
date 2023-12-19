def read_input(file_path):
    """Reads the input file and returns the instructions and node map."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    instructions = lines[0].strip()
    node_map = {}
    for line in lines[1:]:
        if line.strip():
            node, neighbors = line.strip().split(" = ")
            neighbors = tuple(neighbors.strip("()").split(", "))
            node_map[node] = neighbors

    return instructions, node_map

def follow_instructions(instructions, node_map):
    """Follows the instructions from the starting node AAA to reach ZZZ."""
    current_node = 'AAA'
    steps = 0
    instruction_index = 0

    while current_node != 'ZZZ':
        direction = instructions[instruction_index]
        left, right = node_map[current_node]

        current_node = left if direction == 'L' else right
        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return steps

def main():
    file_path = 'input.txt'  # Path to the input file
    instructions, node_map = read_input(file_path)
    steps = follow_instructions(instructions, node_map)
    print(f"Number of steps to reach ZZZ: {steps}")

if __name__ == "__main__":
    main()


# PART TWO
from math import gcd
from functools import reduce

def find_starting_nodes(node_map):
    """Finds all nodes that end with 'A'."""
    return [node for node in node_map.keys() if node.endswith('A')]

def calculate_cycles(instructions, node_map, start_node, occurrences=10):
    """Calculate the number of steps to reach a 'Z'-ending node for a given number of occurrences."""
    current_node = start_node
    steps = 0
    instruction_index = 0
    cycle_steps = []

    while len(cycle_steps) < occurrences:
        if current_node.endswith('Z'):
            cycle_steps.append(steps)
        
        direction = instructions[instruction_index]
        left, right = node_map[current_node]
        current_node = left if direction == 'L' else right
        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)

    return cycle_steps

def lcm(a, b):
    """Calculate the least common multiple of two integers."""
    return abs(a*b) // gcd(a, b)

def main_alignment():
    file_path = 'input.txt'
    instructions, node_map = read_input(file_path)
    starting_nodes = find_starting_nodes(node_map)

    cycle_lengths = []
    for node in starting_nodes:
        cycles = calculate_cycles(instructions, node_map, node)
        print(f"Cycles for node {node}: {cycles}")
        # Calculate cycle length for each node
        cycle_length = cycles[1] - cycles[0]
        cycle_lengths.append(cycle_length)

    # Calculate the LCM of the cycle lengths
    alignment_step = reduce(lcm, cycle_lengths)
    print(f"The step at which all paths align: {alignment_step}")

if __name__ == "__main__":
    main_alignment()

# 15,299,095,336,639