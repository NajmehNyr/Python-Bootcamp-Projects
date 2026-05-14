import random

game_stat = 1; game_over = 0

def deal():
    """Returns a card from our deck.
    Note: Only this function is based on the course solutions."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def write_scores(result):
    """Prints the score of player and computer."""
    player_score = sum(player_cards); comp_score = sum(comp_cards)
    scores = (f"\nYour Score: {player_score}, Computer Score: {comp_score}"
              f"\nYour Cards: {player_cards}, Computer Cards: {comp_cards}")

    if result == "draw": print(f"Draw!{scores}")
    elif result == "bust": print(f"Bust!{scores}")
    elif result == "win": print(f"Win!{scores}")
    elif result == "blackjack": print(f"BlackJack!{scores}")

def win_or_lose():
    """Computes scores and decides if anyone has won or lost while we are drawing cards.
    Returned answer could be used to decide on stopping the game.
    If 5 is returned, the function hasn't done anything on the input."""
    ans = 5
    player_score = sum(player_cards); comp_score = sum(comp_cards)

    if player_score == 21:
        if len(player_cards) == 2: ans = 3
        elif len(player_cards) > 2: ans = 1
    elif comp_score == 21: ans = 0
    elif player_score > 21:
        if 11 in player_cards and player_score - 10 > 21: ans = 0
        else: ans = 0

    if ans == 0: write_scores("bust")
    elif ans == 1: write_scores("win")
    elif ans == 3: write_scores("blackjack")

    return ans

def no_draw_score():
    """If the user didn't draw a new card, it computes the score of the user and computer."""
    ans = 5
    player_score = sum(player_cards); comp_score = sum(comp_cards)

    if comp_score < 21:
        if comp_score > player_score: write_scores("bust"); ans = 0
        elif comp_score == player_score: write_scores("draw"); ans = 2
    elif comp_score == 21: write_scores("bust"); ans = 0
    else: write_scores("win"); ans = 1

    return ans

while game_stat == 1:
    start_button = input('\nDo you want to start the game [y/n]? ')

    # Option 1: Start the game
    if start_button == "y":
        player_cards = []; comp_cards = []

        # Give computer and user 2 cards each
        for _ in range(2):
            player_cards.append(deal())
            comp_cards.append(deal())
        print(f'Computer First Card: [{comp_cards[0]}] \nYour cards:{player_cards}, Your Score: {sum(player_cards)}\n')

        # If the game isn't over in the first hand, continue
        if win_or_lose() != 5: break

        # If they want more cards
        while game_over == 0:
            new_card = input("Do you want to draw another card? [y/n] "); new_card.lower()

            # Yes: Give them a card and compute the scores
            if new_card == "y":
                player_cards.append(deal())
                print(f'Computer First Card: {comp_cards[0]} \nYour cards:{player_cards}, Your Score: {sum(player_cards)}\n')
                if win_or_lose() not in [0, 1]: game_over = 0
                else: game_over = 1

            # No: Draw cards for the computer if the computer score is below 16
            elif new_card == "n":
                while sum(comp_cards) <= 16: comp_cards.append(deal())
                if no_draw_score() != 5 : game_over = 1

            else: print(f"invalid input!"); continue

    # Option 2: Leave the game
    elif start_button == "n": game_stat = 0

    # Option 3: Type an irrelevant answer
    else: print("invalid Input!"); continue

    break
