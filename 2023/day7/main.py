def determinerank(hand):
    counts = {}
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                   '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    numeric_hand = []
    for c in hand:
        numeric_hand.append(card_values[c])
    numeric_hand.sort(reverse=True)

    for card in numeric_hand:
        counts[card] = counts.get(card, 0) + 1

    count_values = []
    for card, count in counts.items():
        count_values.append((count, card))
    count_values.sort(reverse=True)

    hand_type = []
    for count, _ in count_values:
        hand_type.append(count)

    if hand_type == [5]:
        return 7, numeric_hand
    elif hand_type == [4, 1]:
        return 6, numeric_hand
    elif hand_type == [3, 2]:
        return 5, numeric_hand
    elif hand_type == [3, 1, 1]:
        return 4, numeric_hand
    elif hand_type == [2, 2, 1]:
        return 3, numeric_hand
    elif hand_type == [2, 1, 1, 1]:
        return 2, numeric_hand
    else:
        return 1, numeric_hand


def readfile():
    with open('input.txt', 'r') as k:
        hands = k.read().splitlines()
        final_ranks = []
        for line in hands:
            hand, bid = line.split(" ")
            rank, sorted_hand = determinerank(hand)
            final_ranks.append((rank, sorted_hand, int(bid), hand))

        final_ranks.sort(key=lambda x: (x[0], x[1]), reverse=True)

        total_winnings = 0
        num_hands = len(final_ranks)
        for i, (rank, sorted_hand, bid, hand) in enumerate(final_ranks):
            adjusted_rank = num_hands - i
            total_winnings += bid * adjusted_rank
        print(total_winnings)


def main():
    readfile()


if __name__ == '__main__':
    main()
