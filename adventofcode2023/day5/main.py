def parse_mapping_line(line):
    parts = line.split()
    return [int(parts[0]), int(parts[1]), int(parts[2])]

def apply_mapping(num, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= num < src_start + length:
            return dest_start + (num - src_start)
    return num  # If not in any range, return the original number

def process_seed(seed, mappings):
    current_num = seed
    for mapping in mappings:
        current_num = apply_mapping(current_num, mapping)
    return current_num

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Parse seeds
    seeds = [int(x) for x in lines[0].split(': ')[1].split()]

    mappings = []
    current_mapping = None

    for line in lines[1:]:
        if 'map:' in line:
            if current_mapping is not None:
                mappings.append(current_mapping)
            current_mapping = []
        elif line.strip():  # Process non-empty lines
            current_mapping.append(parse_mapping_line(line))

    # Don't forget to add the last mapping
    if current_mapping is not None:
        mappings.append(current_mapping)

    lowest_location = float('inf')
    for seed in seeds:
        location = process_seed(seed, mappings)
        lowest_location = min(lowest_location, location)

    print(f"Lowest location number: {lowest_location}")

if __name__ == "__main__":
    main()


# PART 2
def is_valid_seed_range(num, seed_ranges):
    for start, length in seed_ranges:
        if start <= num < start + length:
            return True
    return False

def reverse_apply_mapping(num, mapping):
    for dest_start, src_start, length in mapping:
        if dest_start <= num < dest_start + length:
            return src_start + (num - dest_start)
    return num  # If not in any range, return the original number

def main_part2():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Parse seed ranges
    seed_values = [int(x) for x in lines[0].split(': ')[1].split()]
    seed_ranges = [(seed_values[i], seed_values[i + 1]) for i in range(0, len(seed_values), 2)]

    print("Parsed Seed Ranges:", seed_ranges)

    mappings = []
    current_mapping = None

    for line in lines[1:]:
        if 'map:' in line:
            if current_mapping is not None:
                mappings.append(current_mapping)
            current_mapping = []
        elif line.strip():  # Process non-empty lines
            current_mapping.append(parse_mapping_line(line))

    # Don't forget to add the last mapping
    if current_mapping is not None:
        mappings.append(current_mapping)

    # Reverse mappings for backward processing
    reverse_mappings = mappings[::-1]

    print("Reverse Mappings:", reverse_mappings)

    # OK to start at 200M... 
    # Part 1 was 389,056,265
    # So it should be at least less than that. 
    # This runs pretty hot so gonna let my laptop cool off for the next 200M
    # Oh weird now this says 200M was valid? that's super weird did I not actually let it run to 200M? 
    # Ugh was that only 20M that I let it run to? fff
    # Nothing from 0 to 20M, 100M to 120M
    location = 135000000
    while True:
        current_num = location

        for mapping in reverse_mappings:
            current_num = reverse_apply_mapping(current_num, mapping)

        if is_valid_seed_range(current_num, seed_ranges):
            print(f"Valid Seed Found! Location: {location}, Seed: {current_num}")
            print(f"Lowest location number: {location}")
            return

        print(f"Checking Location: {location}, Corresponding Seed: {current_num}")

        location += 1

if __name__ == "__main__":
    main_part2()
