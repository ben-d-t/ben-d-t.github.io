# Part 1

# Read in data from input.txt and convert each line to an array item
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initiate a variable for the running total
running_total = 0

# Process each line in the array
for line in lines:
    # Finding the first digit from left to right
    first_digit = None
    for char in line:
        if char.isdigit():
            first_digit = char
            break

    # Finding the first digit from right to left
    second_digit = None
    for char in reversed(line):
        if char.isdigit():
            second_digit = char
            break

    # Forming a two-digit number and adding to the running total
    if first_digit and second_digit:
        number = int(first_digit + second_digit)
        running_total += number

# Print out the total
print(running_total)

# Part 2

# Dictionary to map spelled-out digits to their numeric equivalents
digit_map = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Function to find the first and last digit (numeric or spelled out) in a string
def find_first_and_last_digit(line):
    first_digit, last_digit = None, None

    # Search for the first digit
    for i in range(len(line)):
        for word in digit_map:
            if line[i:i+len(word)] == word:
                if not first_digit:
                    first_digit = digit_map[word]
                last_digit = digit_map[word]
                break
        if line[i].isdigit():
            if not first_digit:
                first_digit = line[i]
            last_digit = line[i]

    return first_digit, last_digit

# Read in data from input.txt and convert each line to an array item
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initiate a variable for the running total
running_total = 0

# Process each line in the array
for line in lines:
    first_digit, last_digit = find_first_and_last_digit(line.strip())

    # Forming a two-digit number and adding to the running total
    if first_digit is not None and last_digit is not None:
        number = int(first_digit + last_digit)
        running_total += number

# Print out the total
print(running_total)