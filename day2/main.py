scores = {"X": 1, "Y": 2, "Z": 3}


def part1():
    win = {"A Y", "B Z", "C X"}
    draw = {"A X", "B Y", "C Z"}

    with open('input.txt', 'r') as k:
        total_score = 0
        for items in k.read().splitlines():
            my_move = items.split(' ')[1]
            if items in win:
                total_score = total_score + 6
            elif items in draw:
                total_score = total_score + 3
            total_score = total_score + scores[my_move]
    print(total_score)


def part2():
    win = {"A Z", "B Z", "C Z"}
    draw = {"A Y", "B Y", "C Y"}
    lose = {"A X", "B X", "C X"}

    loses_to = {"A": "Y", "B": "Z", "C": "X"}
    draw_to = {"A": "X", "B": "Y", "C": "Z"}
    wins_to = {"A": "Z", "B": "X", "C": "Y"}

    with open('input.txt', 'r') as k:
        total_score = 0
        for items in k.read().splitlines():
            computer_move = items.split(' ')[0]
            if items in win:
                total_score = total_score + 6
                total_score = total_score + scores[loses_to[computer_move]]
            elif items in draw:
                total_score = total_score + 3
                total_score = total_score + scores[draw_to[computer_move]]
            elif items in lose:
                total_score = total_score + scores[wins_to[computer_move]]
    print(total_score)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()
