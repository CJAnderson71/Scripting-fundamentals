from random import seed, choice

# Define the suits, numbers, and seed
suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set(range(2, 15))
a = 551
seed(a)

# Function to create a standard deck
def create_standard_deck():
    deck = [(suit, num) for suit in suits for num in numbers]
    return deck

# Function to draw a card from the deck
def draw_card(deck):
    if not deck:
        return None
    card = choice(deck)
    deck.remove(card)
    return card

# Function to display the dealer's hand
def display_dealer(opponent, start=False):
    print('Dealer:')
    if start:
        the_output = [opponent[0], ('?', '?')]
        print(the_output)
    else:
        print(opponent)

# Function to display the player's hand
def display_player(player):
    print('Player:')
    print(player)

# Function to calculate the total value of a player's hand
def get_count(player):
    total = sum(card[1] for card in player)
    # Handle the special case of Aces
    for card in player:
        if card[1] == 14 and total > 21:
            total -= 10  # Change the value of Ace from 14 to 1
    return total

# Function to check if a player has won, busted, or is okay
def check_cards(player):
    total = get_count(player)
    if total == 21:
        return 'WIN'
    elif total > 21:
        return 'BUST'
    else:
        return 'OK'

# Function to create and play the blackjack game
def create_blackjack_game(user_input=None):
    # Create deck and player hands
    deck = create_standard_deck()
    player = [draw_card(deck), draw_card(deck)]
    dealer = [draw_card(deck), draw_card(deck)]

    # Display initial hands
    display_player(player)
    display_dealer(dealer, start=True)

    # Player's turn
    while True:
        player_action = user_input.pop(0) if user_input else input('Press h to hit, s to stand, q to quit: ').lower()
        if player_action == 'q':
            return 0
        elif player_action == 'h':
            card = draw_card(deck)
            player.append(card)
            display_player(player)
            result = check_cards(player)
            if result == 'WIN':
                return 1
            elif result == 'BUST':
                return -1
        elif player_action == 's':
            break

    # Dealer's turn
    while get_count(dealer) < 17:
        card = draw_card(deck)
        dealer.append(card)
        display_dealer(dealer)
        result = check_cards(dealer)
        if result == 'WIN':
            return -1
        elif result == 'BUST':
            return 1

    # Compare hands
    player_total = get_count(player)
    dealer_total = get_count(dealer)

    if player_total > dealer_total:
        return 1
    elif player_total < dealer_total:
        return -1
    else:
        return 0

# Test the game
result = create_blackjack_game(["h", "s", "s", "q"])
if result == 1:
    print("Player wins!")
elif result == -1:
    print("Dealer wins!")
else:
    print("It's a tie!")
