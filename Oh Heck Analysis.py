import openpyxl
import csv
import pandas as pd

import pdb
debug = True
#debug = False
def set_trace():
    if debug:
        pdb.set_trace()

def get_row_vals(excel_filename):
    wb = openpyxl.load_workbook(excel_filename, data_only = True)
    sh = wb.get_active_sheet()
    # This is hard coded to the specific spreadsheet format I made
    rows = [[cell.value for cell in row] for row in sh.rows]
    # Remove top three rows without data
    rows = rows[3:]
    # Remove rows with only None values
    rows = [row for row in rows if len([val for val in row if val]) > 0]

    return rows

def extract_data(rows):
    # Extract top row non-None values representing each round
    rounds = [val for val in rows[0] if val]
    rows = rows[1:]
    names = [row[0] for row in rows if row[0]]
    bids = []
    makes = []
    scores = []
    for i in range(len(names)):
        bids_row = []
        makes_row = []
        scores_row = []
        for j in range(len(rounds)):
            bids_row.append(rows[2*i][(2*j)+1])
            makes_row.append(rows[2*i][2*(j+1)])
            scores_row.append(rows[(2*i)+1][2*(j+1)])
        bids.append(bids_row)
        makes.append(makes_row)
        scores.append(scores_row)
    return rounds, names, bids, makes, scores

filename = "Example Spreadsheets/2017.11.21 1 Oh Heck Score Sheet.xlsx"
rows = get_row_vals(filename)
rounds, names, bids, makes, scores = extract_data(rows)


def extract_col(rows, round_index):



    return -1

set_trace()
# with open('test.csv', 'w') as f:
#     c = csv.writer(f)
#     set_trace()
#     for r in sh.rows:
#         c.writerow([cell.value for cell in r])