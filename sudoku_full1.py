import math

def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board


def all_9_boards(board):
    all_boards = [build_gameboard() for board in range(9)]
    board_1, board_2, board_3 = all_boards[0], all_boards[1], all_boards[2]
    board_4, board_5, board_6 = all_boards[3], all_boards[4], all_boards[5]
    board_7, board_8, board_9 = all_boards[6], all_boards[7], all_boards[8]
    board_1[0][1], board_1[0][2], board_1[1][0], board_1[2][0] = 5, 8, 4, 9
    board_2[0][0], board_2[0][1], board_2[1][1] = 9, 2, 7
    board_3[1][0], board_3[1][2], board_3[2][1], board_3[2][2] = 5, 3, 1, 8
    board_4[0][1], board_4[0][2], board_4[1][0] = 9, 7, 2
    board_5[0][0], board_5[0][1], board_5[0][2], board_5[1][0] = 8, 3, 5, 7
    board_5[1][2], board_5[2][0], board_5[2][1], board_5[2][2] = 6, 1, 9, 2
    board_6[1][2], board_6[2][0], board_6[2][1] = 9, 6, 3
    board_7[0][0], board_7[0][1], board_7[1][0], board_7[1][2] = 1, 4, 7, 5
    board_8[1][1], board_8[2][1], board_8[2][2] = 6, 1, 3
    board_9[0][2], board_9[1][2], board_9[2][0], board_9[2][1] = 5, 1, 4, 7 
    return all_boards


def print_all(all_boards):
    board = build_gameboard()
    all_boards = all_9_boards(board)
    i = 0
    while i < len(all_boards):
        for n in range(3):
            (r1, r2, r3) = all_boards[i][n], all_boards[i + 1][n], all_boards[i + 2][n]
            (r1, r2, r3) = [" ".join(str(element) for element in string) 
                                             for string in (r1, r2, r3)]
            print("{:^8s}{:^8s}{:^8s}".format(r1, r2, r3))
        i += 3
        print()


print_all(all_9_boards(build_gameboard()))


def nums_in_rows_and_cols(*args):
    assert len(args) == 9, "all 9 boards must be present!"
    nums_all_boards_rows = []
    a = 0
    while a < len(args):
        for i in range(3):
            nums_in_rows = args[a][i] + args[a + 1][i] + args[a + 2][i]
            nums_all_boards_rows.append(nums_in_rows)
            print(nums_in_rows)
        a += 3
    print()
    nums_all_boards_cols = [[x[i] for x in nums_all_boards_rows] 
                      for i in range(len(nums_all_boards_rows))]
    for item in nums_all_boards_cols:
        print(item)
    return (nums_all_boards_rows, nums_all_boards_cols)


def fill_empty(all_boards):
    board = build_gameboard()
    all_boards = all_9_boards(board)
    b1, b2, b3 = all_boards[0], all_boards[1], all_boards[2]
    b4, b5, b6 = all_boards[3], all_boards[4], all_boards[5]
    b7, b8, b9 = all_boards[6], all_boards[7], all_boards[8]
    
    all_data = nums_in_rows_and_cols(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    all_rows, all_cols = all_data[0], all_data[1]
    
    taken_numbers = {x for row in all_rows for x in row if x != 0}
    aval_numbers = set(range(1, 10)) - taken_numbers
    
    print("Numbers taken: {}".format(taken_numbers))
    print("Numbers available: {}".format(aval_numbers))


fill_empty(all_9_boards(build_gameboard))
