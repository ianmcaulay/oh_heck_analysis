import deck
from extract_hand_data import get_player_hands_data
import analysis
import extract_data

import pdb


# TODO: this should probably be rewritten to create the whole
# vector at the same time rather than doing the hand and game
# data separately. Should make it easier to add information
# whole dataframe and gameID. 


def vectorize_hands_data(num_cards, trumps, hands):
    # Vector is number of cards, trump (len 5 card vector), hand vector (len
    # 52 one hot encoded)

    vectors = []
    for i in range(len(num_cards)):
        vector = []
        vector += [num_cards[i]]
        vector += deck.to_card(trumps[i]).vectorize()
        vector += hands[i].vectorize()
        vectors.append(vector)

    return vectors



filename = "Example Spreadsheets/2017.12.22 1 Oh Heck Score Sheet.xlsx"
num_cards, trumps, hands = get_player_hands_data(filename, "Ian")
vectors = vectorize_hands_data(num_cards, trumps, hands)



pdb.set_trace()




