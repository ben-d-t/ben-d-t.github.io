def card_value(card):
    values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    return values[card] if card in values else int(card)

def classify_hand(hand):
    counts = {card: hand.count(card) for card in set(hand)}
    # Create a pattern string based on the counts of each card, sorted by frequency and value
    pattern = ''.join(sorted([str(counts[card]) for card in counts], reverse=True))

    hand_type = {
        '5': 1,     # Five of a kind
        '41': 2,    # Four of a kind
        '32': 3,    # Full house
        '311': 4,   # Three of a kind
        '221': 5,   # Two pair
        '2111': 6,  # One pair
    }.get(pattern, 7)  # High card or default

    # Return the hand type and the hand in its original order
    return (hand_type, tuple(hand))

def hand_comparator(hand_info):
    hand_type, sorted_hand = hand_info[0]
    return (hand_type, tuple(-card_value(card) for card in sorted_hand))

def read_hands(filename):
    with open(filename, 'r') as file:
        hands = [line.strip().split() for line in file]
    return [(hand[0], int(hand[1])) for hand in hands]

def sort_hands_by_type(hands, classifier_func, comparator_func):
    categorized_hands = [(classifier_func(hand), bid) for hand, bid in hands]

    # Sort hands using the provided comparator function
    categorized_hands.sort(key=comparator_func)

    return categorized_hands



def calculate_winnings(sorted_hands):
    total_winnings = 0
    total_hands = len(sorted_hands)
    for rank, ((_, _), bid) in enumerate(sorted_hands, start=1):
        adjusted_rank = total_hands - rank + 1
        total_winnings += adjusted_rank * bid
    return total_winnings


def main():
    hands = read_hands("input.txt")
    sorted_hands = sort_hands_by_type(hands, classify_hand, hand_comparator)
    total_hands = len(sorted_hands)

    # Print the first 20 hands in sorted_hands along with bid calculation details
    print("First 20 ranked hands with bid calculation details:")
    for i, ((hand_type, sorted_hand), bid) in enumerate(sorted_hands):
        if i >= 20:
            break
        adjusted_rank = total_hands - i  # Adjust rank according to game rules
        winnings_for_hand = adjusted_rank * bid
        print(f"{adjusted_rank}: Hand: {''.join(sorted_hand)}, Type: {hand_type}, Bid: {bid}, Adjusted Rank * Bid = {winnings_for_hand}")

    winnings = calculate_winnings(sorted_hands)
    print(f"\nTotal winnings: {winnings}")

if __name__ == "__main__":
    main()

# PART TWO
def card_value_joker(card):
    values = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, 'J': 1}  # J is now weakest
    return values[card] if card in values else int(card)

def hand_comparator_joker(hand_info):
    hand_type, sorted_hand = hand_info[0]
    # Convert each card to its value with Jokers as the weakest
    card_values = tuple(-card_value_joker(card) for card in sorted_hand)
    return (hand_type, card_values)


def classify_hand_with_joker(hand):
    # Count each card, treating Jokers separately
    counts = {card: hand.count(card) for card in set(hand) if card != 'J'}
    #print(counts)
    joker_count = hand.count('J')
    #print(joker_count)

    # Determine the best hand type possible with Jokers
    best_hand_type = determine_best_hand_type_with_joker(counts, joker_count)

    # Return the hand in its original order along with its best possible type
    return (best_hand_type, tuple(hand))

def determine_best_hand_type_with_joker(counts, joker_count):
    # Sort counts for checking hand types
    sorted_counts = sorted(counts.values(), reverse=True)

    # Check for Five of a Kind
    if joker_count == 5:
        return 1 # Five of a Kind jokers
    if joker_count + sorted_counts[0] == 5:
        return 1  # Five of a Kind

    # Check for Four of a Kind
    if sorted_counts[0] == 4 or (joker_count + sorted_counts[0] == 4):
        return 2  # Four of a Kind

    # Check for Full House
    if (sorted_counts[0] == 2 and sorted_counts[1] == 2 and joker_count == 1) or (sorted_counts[0] == 3 and sorted_counts[1] == 2):
        return 3  # Full House

    # Check for Three of a Kind, Two Pair, One Pair
    if sorted_counts[0] == 3 or (joker_count + sorted_counts[0] == 3):
        return 4  # Three of a Kind
    if (len(sorted_counts) >= 2 and sorted_counts[1] == 2):
        return 5  # Two Pair
    if sorted_counts[0] == 2 or joker_count == 1:
        return 6  # One Pair

    return 7  # High Card



def main_part2():
    hands = read_hands("input.txt")
    sorted_hands = sort_hands_by_type(hands, classify_hand_with_joker, hand_comparator_joker)  # Modify sort_hands_by_type to accept classifier function as argument
    total_hands = len(sorted_hands)

    # Print the first 20 hands in sorted_hands along with bid calculation details
    print("First 20 ranked hands with bid calculation details:")
    for i, ((hand_type, sorted_hand), bid) in enumerate(sorted_hands):
        if i >= 2000:
            break
        adjusted_rank = total_hands - i  # Adjust rank according to game rules
        winnings_for_hand = adjusted_rank * bid
        print(f"{adjusted_rank}: Hand: {''.join(sorted_hand)}, Type: {hand_type}, Bid: {bid}, Adjusted Rank * Bid = {winnings_for_hand}")

    winnings = calculate_winnings(sorted_hands)
    print(f"\nTotal winnings PART TWO: {winnings}")

if __name__ == "__main__":
    main_part2()

# 252514050 is too LOW
# 252537161 is also too low
# 253631952 is too HIGH dangit
# 253810806 frit that must be wrong
# 253473930
# Huh this is the first part that ChatGPT just couldn't handle building the logic
# For Day5 Part Two I had to solve it myself w/ some guess + check, but ChatGPT was at least building the functions well. 
# But for this, I should've realized sooner that ChatGPT's implementation of the typing was wrong... 