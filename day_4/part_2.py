boards = []

def check_for_win():

    for board in boards:

        # check for vertical row
        for column in range(5):
            tally = 0
            for row in range(5):
                if board["rows"][row][column]["marked"]:
                    tally += 1
                    if tally >= 5: 
                        board["has_won"] = True

        # check for horizontal row
        for i, row in enumerate(board["rows"]):
            marked = [x for x in row if x["marked"]]
            if len(marked) >= 5: 
                board["has_won"] = True



def all_have_won():
    if not [board for board in boards if not board["has_won"]]:
        print("all the boards have won")
        return True


def play_bingo(draw_numbers):
    for draw_number in draw_numbers:
        for board in boards:
            for row in board["rows"]:
                for number in row:
                    if number["value"] == draw_number:
                        number["marked"] = True
                        check_for_win()
                        if all_have_won(): return board, draw_number


def calculate_score(board):
    tally = 0

    for row in board["rows"]:
        for number in row:
            if not number["marked"]:
                tally += number["value"]

    return tally


if __name__ == "__main__":
    raw_input = open("input.txt", "r").read()
    lines = raw_input.splitlines()

    draw_numbers = [int(i) for i in lines[0].split(",")]

    for i in range(2, len(lines), 6):
        board = {
            "has_won": False,
            "rows": []
        }
        for j in range(5):
            row = []
            line_numbers = lines[i + j].split()
            for number in line_numbers:
                row.append({
                    "marked": False,
                    "value": int(number)
                })
            board["rows"].append(row)
        boards.append(board)
    
    winning_board, winning_number = play_bingo(draw_numbers)

    print(
        calculate_score(winning_board) * winning_number
    )
