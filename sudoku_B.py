
def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board


def print_board(board):
    boardstring = "\n".join(str(row) for row in board)
    return boardstring


def all_9_boards(board):
    all_boards = [build_gameboard() for board in range(9)]
    return all_boards


def print_all(all_boards):
    board = build_gameboard()
    all_boards = all_9_boards(board)
    i = 0
    while i < 9:
        for n in range(3):
            (r1, r2, r3) = all_boards[i][n], all_boards[i + 1][n], all_boards[i + 2][n]
            (r1, r2, r3) = [" ".join(str(element) for element in string) 
                                             for string in (r1, r2, r3)]
            print("{:^8s}{:^8s}{:^8s}".format(r1, r2, r3))
        i += 3
        print()


print_all(print_board(build_gameboard()))
