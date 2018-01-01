

import pdb

#suits = {"C": 1, "D": 2, "H": 3, "S": 4}
num_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
              "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

class Suit:

    def __init__(self, letter, name, index):
        self.letter = letter
        self.name = name
        self.index = index

class Value:

    def __init__(self, string, name, val):
        self.string = string
        self.name = name
        self.val = val


clubs = Suit("C", "Clubs", 0)
diamonds = Suit("D", "Diamonds", 1)
hearts = Suit("H", "Hearts", 2)
spades = Suit("S", "Spades", 3)
suits = {"C": clubs, "D": diamonds, "H": hearts, "S": spades}

two = Value("2", "Two", 2)
three = Value("3", "Three", 3)
four = Value("4", "Four", 4)


class Card:

    def __init__(self, suit, value):

        self.suit = suit
        self.value = value


def is_valid_card(card_str):
    """ 
    Check whether the given string is in a valid
    format to represent a card. First character should be
    the suit and the second should be the number (10s 
    are the only cards with three characters)
    """
    # TODO: could do some error correction where rather just returning false it attempts to fix common errors like the number coming before the suit, 1 instead of A, etc.

    card_str = card_str.upper()
    if len(card_str) < 2 or len(card_str) > 3:
        return False
    if card_str[0] not in suits:
        return False
    if len(card_str) == 2 and card_str[1] not in num_values:
        return False
    if len(card_str) == 3 and card_str[1:] != "10":
        return False
    return True




def vectorize_card(card):

    suit_index =

    return []




