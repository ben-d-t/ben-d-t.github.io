def calculate_points(filename):
    total_points = 0

    with open(filename, 'r') as file:
        for line in file:
            # Splitting the line into parts and ignoring the initial "Card X:" part
            _, card_data = line.split(':', 1)
            winning_numbers, your_numbers = card_data.split('|')
            winning_numbers = set(map(int, winning_numbers.split()))
            your_numbers = set(map(int, your_numbers.split()))

            matches = winning_numbers.intersection(your_numbers)
            points = 1 if matches else 0
            for _ in range(len(matches) - 1):
                points *= 2
            
            total_points += points

    return total_points

# Call the function with the filename
filename = 'input.txt'
total_points = calculate_points(filename)
print(f"Total points: {total_points}")

# PART 2
def process_cards(filename):
    with open(filename, 'r') as file:
        cards = [line.strip().split(':', 1)[1] for line in file]

    def count_matches(card):
        winning_numbers, your_numbers = card.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))
        return len(winning_numbers.intersection(your_numbers))

    total_cards = 0
    card_counts = [1] * len(cards)  # Initialize with 1 for each original card

    for i in range(len(cards)):
        matches = count_matches(cards[i])
        total_cards += card_counts[i]  # Count this card and its copies

        # Add copies to subsequent cards
        for j in range(1, matches + 1):
            if i + j < len(cards):
                card_counts[i + j] += card_counts[i]

    return total_cards

# Call the function with the filename
filename = 'input.txt'
total_cards = process_cards(filename)
print(f"Total number of scratchcards: {total_cards}")
