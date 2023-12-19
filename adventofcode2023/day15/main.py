def hash_algorithm(step):
    current_value = 0
    for char in step:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def process_sequence(sequence):
    steps = sequence.split(',')
    total = sum(hash_algorithm(step) for step in steps)
    return total

def main():
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    result = process_sequence(data)
    print("The sum of the results is:", result)

if __name__ == "__main__":
    main()
