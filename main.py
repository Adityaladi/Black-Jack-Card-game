import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    """A cards game"""
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game != "y":
        exit()
    your_cards = []
    dealer_cards = []

    for x in range(2):
        your_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

    def more_card():
        dealer_score = None
        current_score = None
        ace = 11
        dealer_score = sum(dealer_cards)
        current_score = sum(your_cards)
        if dealer_score < 16:
            dealer_cards.append(random.choice(cards))
            dealer_score = sum(dealer_cards)
        if ace in your_cards and current_score > 21:
            i = your_cards.index(11)
            your_cards[i] = 1
            current_score = sum(your_cards)
        if ace in dealer_cards and dealer_score > 21:
            j = dealer_cards.index(11)
            dealer_cards[j] = 1
            dealer_score = sum(dealer_cards)

        print(f"Your cards: {your_cards}, Current_score: {current_score}\nComputer's first card: {dealer_cards[0]}")

        if current_score > 21:
            print("You went over. You lose 😭")
            blackjack()

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            your_cards.append(random.choice(cards))
            more_card()
        elif another_card == "n":
            print(
                f"Your final hand: {your_cards}, final_score: {current_score}\nComputer's final hand: {dealer_cards}, final score: {dealer_score}")

        if dealer_score > 21:
            print("Dealer went over. You win")
            blackjack()
        elif dealer_score > current_score:
            print("you lose")
            blackjack()
        elif dealer_score == current_score:
            print("draw")
            blackjack()
        else:
            print("you win")
            blackjack()

    more_card()


blackjack()
