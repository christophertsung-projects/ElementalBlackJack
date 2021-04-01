import random

class Card:
    card_suit = ""

class Suit:
    card_list = []
    def __init__(self, suit):
        self.card_suit = suit
        self.card_list = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", 'Q', "K"]
    def draw_card(self):
        random_number = random.randint(0, 13)
        card = self.card_list[random_number]
        self.card_list.remove(random_number)
        return card

class Deck:
    suit_count = 0
    suit_list = []
    def __init__(self, number_of_decks):
        self.suit_count = number_of_decks * 4
        for x in range(number_of_decks):
            self.suit_list.append(Suit("Earth"))
            self.suit_list.append(Suit("Fire"))
            self.suit_list.append(Suit("Water"))
            self.suit_list.append(Suit("Air"))
    def draw(self):
        random_number = random.randint(0, len(self.suit_list) - 1)
        card = self.suit_list[random_number].draw_card
        if (len(self.suit_list[random_number]) == 0):
            self.suit_list.remove(random_number)
        return card

class Player:
    name = ""
    hand = []
    def __init__(self, name):
        self.name = name

game_continuing = True
while game_continuing:
    print("Welcome to ELEMENTAL BLACKJACK!")
    number_of_decks = int(input("Please enter how many decks you want in the game:"))
    deck = Deck(number_of_decks)
    players = []
    number_of_players = int(input("Enter the number of players, now!:"))
    for x in range(number_of_players):
        players.append(Player(input("Enter player " + str(x + 1) + "'s name, or else!:")))
    for x in players:
        players[x].hand.append(deck.draw())
        players[x].hand.append(deck.draw())
        turn_continuing = True
        while turn_continuing:
            print("Would you like to hit(h) or stay(s)? Your cards are: " )
