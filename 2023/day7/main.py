import functools

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
               '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
card_values2 = {'A': 13, 'K': 12, 'Q': 11, 'T': 10,
                '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def calculate_hand(hand):
    numeric_hand = []
    counts = {}

    for c in hand:
        numeric_hand.append(card_values[c])
    numeric_hand.sort(reverse=True)

    for card in numeric_hand:
        counts[card] = counts.get(card, 0) + 1

    count_values = []
    for card, count in counts.items():
        count_values.append((count, card))
    count_values.sort(reverse=True)

    final_counts = []
    for count, _ in count_values:
        final_counts.append(count)

    if final_counts == [5]:
        return 1
    elif final_counts == [4, 1]:
        return 2
    elif final_counts == [3, 2]:
        return 3
    elif final_counts == [3, 1, 1]:
        return 4
    elif final_counts == [2, 2, 1]:
        return 5
    elif final_counts == [2, 1, 1, 1]:
        return 6
    else:
        return 7


def compare(hand1, hand2):
    level1, level2 = calculate_hand(hand1[0]), calculate_hand(hand2[0])
    if level1 != level2:
        return level1 - level2

    for card1, card2 in zip(hand1[0], hand2[0]):
        result = card_values[card2] - card_values[card1]
        if result != 0:
            return result
    return 0


def compare_with_joker(hand1, hand2):
    level1, level2 = calculate_hand_with_joker(hand1[0]), calculate_hand_with_joker(hand2[0])
    if level1 != level2:
        return level1 - level2

    for card1, card2 in zip(hand1[0], hand2[0]):
        if card1 == 'J' and card2 != 'J':
            return 1
        elif card2 == 'J' and card1 != 'J':
            return -1
        else:
            result = card_values2[card1] - card_values2[card2]
            if result != 0:
                return result
    return 0


def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    hands_bids = []
    for line in lines:
        hand, bid = line.split(" ")
        hands_bids.append((hand, int(bid)))

    n = len(hands_bids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(hands_bids[j], hands_bids[j + 1]) < 0:
                hands_bids[j], hands_bids[j + 1] = hands_bids[j + 1], hands_bids[j]

    total_winnings = 0
    for index, (_, bid) in enumerate(hands_bids):
        total_winnings += bid * (index + 1)

    print(total_winnings)


def calculate_hand_with_joker(hand):
    counts = {}
    joker_count = hand.count('J')
    hand_without_jokers = [card for card in hand if card != 'J']

    for card in hand_without_jokers:
        counts[card] = counts.get(card, 0) + 1

    if not counts:
        counts['A'] = joker_count  # Hypothetically considering jokers as 'A' for the strongest hand
    else:
        most_common_card, most_common_count = max(counts.items(), key=lambda x: (x[1], card_values2[x[0]]))
        counts[most_common_card] += joker_count

    count_values = sorted(counts.values(), reverse=True)

    if count_values == [5]:
        return 1
    elif count_values == [4, 1]:
        return 2
    elif count_values == [3, 2]:
        return 3
    elif count_values == [3, 1, 1]:
        return 4
    elif count_values == [2, 2, 1]:
        return 5
    elif count_values == [2, 1, 1, 1]:
        return 6
    else:
        return 7


def part2():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    hands_bids = [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]

    hands_bids.sort(key=functools.cmp_to_key(compare_with_joker), reverse=True)

    total_winnings = sum(bid * (index + 1) for index, (_, bid) in enumerate(hands_bids))
    print(total_winnings)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
