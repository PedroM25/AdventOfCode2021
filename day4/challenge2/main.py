# things that are assumed:
# - file ends with empty line

def read_file():
    with open("../input.txt", "r") as f:
        global bingo_numbers
        bingo_numbers = f.readline().removesuffix("\n").split(",")

        global all_bingo_cards
        all_bingo_cards = []

        current_bingo_card = []
        for line in f:
            if line == "\n":
                if len(current_bingo_card) != 0:
                    all_bingo_cards.append(current_bingo_card)
                    current_bingo_card = []
                continue
            current_bingo_card.append([(x, False) for x in line.removesuffix("\n").split()])
        all_bingo_cards.append(current_bingo_card)


def is_winner_card(card_no, pos_tuple):
    card = all_bingo_cards[card_no]
    x = pos_tuple[0]
    y = pos_tuple[1]

    # winning line (analyzes whole line at once)
    if all([marking for (_, marking) in card[x]]):
        return True

    # winning column (analyzes each value in column, one by one)
    for line in card:
        if not line[y][1]:
            return False
    return True


def pos_in_card(card_no, number):
    card = all_bingo_cards[card_no]

    for line_no in range(len(card)):
        for col_no in range(len(card[line_no])):
            if card[line_no][col_no][0] == number:
                card[line_no][col_no] = (card[line_no][col_no][0], True)
                return line_no, col_no
    return ()


def add_all_unmarked_numbers(card_no):
    card = all_bingo_cards[card_no]
    to_ret = 0
    for line in card:
        for (no, marking) in line:
            if not marking:
                to_ret += int(no)
    return to_ret


all_bingo_cards = []
bingo_numbers = []


# the first card that wins
def main():
    read_file()
    winner_cards = [False] * len(all_bingo_cards)
    for number in bingo_numbers:
        for card_no in range(len(all_bingo_cards)):
            if winner_cards[card_no]:
                continue

            pos = pos_in_card(card_no, number)
            if pos == ():
                continue

            if is_winner_card(card_no, pos):
                winner_cards[card_no] = True
                if all(winner_cards):
                    return int(number) * add_all_unmarked_numbers(card_no)


if __name__ == "__main__":
    print(main())
