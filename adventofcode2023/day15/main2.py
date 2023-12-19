def hash_algorithm(label):
    current_value = 0
    for char in label:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def process_step(boxes, step):
    if '=' in step:
        label, focal_length = step.split('=')
        focal_length = int(focal_length)
        operation = '='
    else:
        label = step[:-1]
        operation = '-'

    box_index = hash_algorithm(label)

    if operation == '-':
        boxes[box_index] = [lens for lens in boxes[box_index] if lens[0] != label]
    else:
        found = False
        for i, lens in enumerate(boxes[box_index]):
            if lens[0] == label:
                boxes[box_index][i] = (label, focal_length)
                found = True
                break
        if not found:
            boxes[box_index].append((label, focal_length))

def print_boxes(boxes, step):
    print(f'After "{step}":')
    for i, box in enumerate(boxes):
        if box:
            lenses = ' '.join([f'[{label} {focal_length}]' for label, focal_length in box])
            print(f'Box {i}: {lenses}')

def calculate_focusing_power(boxes):
    total_power = 0
    for box_index, lenses in enumerate(boxes):
        for slot_index, (label, focal_length) in enumerate(lenses, start=1):
            total_power += (box_index + 1) * slot_index * focal_length
    return total_power

def main():
    boxes = [[] for _ in range(256)]
    with open('input.txt', 'r') as file:
        data = file.read().replace('\n', '')
    steps = data.split(',')
    for step in steps:
        process_step(boxes, step)
        print_boxes(boxes, step)
    result = calculate_focusing_power(boxes)
    print("\nThe total focusing power is:", result)

if __name__ == "__main__":
    main()
