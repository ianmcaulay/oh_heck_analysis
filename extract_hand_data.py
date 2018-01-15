import pandas as pd
import openpyxl
import deck
#from os import listdir

import pdb


def get_player_hands_data(excel_filename, player_name):
    wb = openpyxl.load_workbook(excel_filename, data_only = True)
    sh = wb.get_sheet_by_name(player_name)
    # This is hard coded to the specific spreadsheet format I made
    rows = [[cell.value for cell in row if cell.value] for row in sh.rows]
    # Remove top two rows without data
    rows = rows[2:]
    # Extract and remove the number of cards and trump cards
    num_cards = [row[0] for row in rows]
    trumps = [row[1] for row in rows]
    rows = [row[2:] for row in rows]
    hands = []
    for row in rows:
        hands.append(convert_row_to_hand(row))

    return num_cards, trumps, hands


def convert_row_to_hand(row):
    cards = []
    for card_str in row:
        cards.append(deck.to_card(card_str))
    return deck.Hand(cards)


#filename = "Example Spreadsheets/2017.12.22 1 Oh Heck Score Sheet.xlsx"
#num_cards, trumps, hands = get_player_hands_data(filename, "Ian")