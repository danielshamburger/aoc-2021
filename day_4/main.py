

def check_for_win(board):

    # check for vertical row
    for column in range(5):
        tally = 0
        for row in range(5):
            if board[row][column]["marked"]:
                tally += 1
                if tally >= 5: return True

    # check for horizontal row
    for i, row in enumerate(board):
        marked = [x for x in row if x["marked"]]
        if len(marked) >= 5: return True


def play_bingo(draw_numbers, boards):
    for draw_number in draw_numbers:
        for board in boards:
            for row in board:
                for number in row:
                    if number["value"] == draw_number:
                        number["marked"] = True
                        if check_for_win(board): return board, draw_number


def calculate_score(board):
    tally = 0

    for row in board:
        for number in row:
            if not number["marked"]:
                tally += number["value"]

    return tally


if __name__ == "__main__":
    raw_input = open("sample.txt", "r").read()
    lines = raw_input.splitlines()

    draw_numbers = [int(i) for i in lines[0].split(",")]

    boards = []
    for i in range(2, len(lines), 6):
        board = []
        for j in range(5):
            row = []
            line_numbers = lines[i + j].split()
            for number in line_numbers:
                row.append({
                    "marked": False,
                    "value": int(number)
                })
            board.append(row)
        boards.append(board)
    
    winning_board, winning_number = play_bingo(draw_numbers, boards)

    print(
        calculate_score(winning_board) * winning_number
    )
