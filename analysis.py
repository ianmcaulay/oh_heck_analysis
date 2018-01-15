import csv
import pandas as pd
from extract_data import get_df_from_excel, extract_all_data


import pdb
debug = True
#debug = False
def set_trace():
    if debug:
        pdb.set_trace()


def get_player_df(df, player):
    return df.loc[df['Player'] == player]

def get_tricks_bid_percentage(df, player):
    df = get_player_df(df, player)
    return df['Bid'].sum() / df['Round'].sum()

def get_tricks_made_percentage(df, player):
    df = get_player_df(df, player)
    return df['Made'].sum() / df['Round'].sum()

def get_make_percentage(df, player):
    df = get_player_df(df, player)
    made_df = df[df['Bid'] == df['Made']]
    return len(made_df) / len(df)

def get_underbid_percentage(df, player):
    df = get_player_df(df, player)
    made_df = df[df['Bid'] < df['Made']]
    return len(made_df) / len(df)

def get_overbid_percentage(df, player):
    df = get_player_df(df, player)
    made_df = df[df['Bid'] > df['Made']]
    return len(made_df) / len(df)

def get_final_score_rows(df):
    return df[df['Round'] == 1]

def repeat_for_all_players(df, fn):
    players = set(df['Player'])
    results = []
    for player in players:
        res = fn(df, player)
        results.append([player, res])
    results = sorted(results, key=lambda result: result[1])
    for res in results:
        print(res[0] + " had result " + str(res[1]))

rep = repeat_for_all_players


#filename = "Example Spreadsheets/2017.11.21 1 Oh Heck Score Sheet.xlsx"
folderpath = "Example Spreadsheets"
#df = get_df_from_excel(filename)
df = extract_all_data(folderpath)
set_trace()

