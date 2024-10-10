suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Player:
    pass

class Deck:
    def __init__(self, player_count):
        self.cards = []
        self.player_count = player_count
        self.ranks = ranks[:]
        self.reset()

    def reset(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def get_lowest_rank(self):
        return self.ranks[0]
