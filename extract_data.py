import pandas as pd
import openpyxl

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


def create_df():
    cols = ["GameID", "Player", "Round", "Bid", "Made", "Score"]
    return pd.DataFrame(columns=cols)


def add_row_data_to_df(rows, df, game_id):
    rounds, names, bids, makes, scores = extract_data(rows)
    for i in range(len(rounds)):
        for j in range(len(names)):
            new_row = {"GameID": game_id}
            new_row["Player"] = names[j]
            new_row["Round"] = rounds[i]
            new_row["Bid"] = bids[j][i]
            new_row["Made"] = makes[j][i]
            new_row["Score"] = scores[j][i]
            df = df.append(new_row, ignore_index=True)
    return df


def make_game_id_from_filename(filename):
	# Remove the last slash and everything before it
	filename = filename[filename.rfind("/")+1:]
	# Remove the last dot and everything after it
	filename = filename[:filename.rfind(".")]
	filename = filename.lower()
	filename = filename.replace("oh", "")
	filename = filename.replace("heck", "")
	filename = filename.replace("score", "")
	filename = filename.replace("sheet", "")
	filename.replace("  ", " ")
	return filename


def verify_data(rounds, names, bids, makes, scores):
    """
    Perform checks to make sure the data was formatted and read
    correctly, i.e. scores are correct, lens of each person and
    round match up, etc.
    """
    # TODO: implement this
    return False


def get_df_from_excel(excel_filename):
	df = create_df()
	rows = get_row_vals(excel_filename)
	game_id = make_game_id_from_filename(excel_filename)
	df = add_row_data_to_df(rows, df, game_id)
	return df


def extract_all_data(data_folder):
	
	df = create_df()
	#for filename in data_folder:
		# append get_df_from_excel(filename)

	return df




