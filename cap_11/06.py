from random import shuffle
from 04 import FrenchDeck

# (self, key, value)
def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card


deck = FrenchDeck()

shuffle(deck)


