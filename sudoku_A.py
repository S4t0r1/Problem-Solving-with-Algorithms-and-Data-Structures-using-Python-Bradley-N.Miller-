
def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board


def print_board(board):
    boardstring = "\n".join(str(row) for row in board)
    return boardstring


def all_9_boards(board):
    all_boards = [[build_gameboard() for board in range(3)] for boards_row in range(3)]
    return all_boards


def print_all(all_boards):
    board = build_gameboard()
    all_boards = all_9_boards(board)
    for boards_row in all_boards:
        for i in range(3):
            print("   ".join([str(boards_row[n][i]) for n in range(3)]))
        print()


print_all(print_board(build_gameboard()))
