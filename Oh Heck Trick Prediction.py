

class Suit:
    def __init__(self, letter, name, index):
        self.letter = letter.upper()
        self.name = name
        self.index = index


class Value:
    def __init__(self, string, name, val):
        self.string = string
        self.name = name
        self.val = val


class Card:
    def __init__(self, suit, value):

        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value.name + " of " + self.suit.name

    def __str__(self):
        return self.value.name + " of " + self.suit.name


def create_suits():

    clubs = Suit("C", "Clubs", 0)
    diamonds = Suit("D", "Diamonds", 1)
    hearts = Suit("H", "Hearts", 2)
    spades = Suit("S", "Spades", 3)
    return {"C": clubs, "D": diamonds, "H": hearts, "S": spades}


def create_values():
    two = Value("2", "Two", 2)
    three = Value("3", "Three", 3)
    four = Value("4", "Four", 4)
    five = Value("5", "Five", 5)
    six = Value("6", "Six", 6)
    seven = Value("7", "Seven", 7)
    eight = Value("8", "Eight", 8)
    nine = Value("9", "Nine", 9)
    ten = Value("10", "Ten", 10)
    jack = Value("J", "Jack", 11)
    queen = Value("Q", "Queen", 12)
    king = Value("K", "King", 13)
    ace = Value("A", "Ace", 14)
    return {"2": two, "3": three, "4": four, "5": five, "6": six,
            "7": seven, "8": eight, "9": nine, "10": ten,
            "J": jack, "Q": queen, "K": king, "A": ace}


suits = create_suits()
values = create_values()


def create_deck():
    deck = []
    for suit in suits.values():
        for value in values.values():
            deck.append(Card(suit, value))
    return deck


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

    card_vector = [0] * 5
    card_vector[card.suit.index] = 1
    card_vector[4] = card.value.val
    return card_vector


deck = create_deck()
vectors = [vectorize_card(card) for card in deck]


