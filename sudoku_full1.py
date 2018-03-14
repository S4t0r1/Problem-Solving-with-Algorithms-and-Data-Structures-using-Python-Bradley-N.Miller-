import math, string

def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board

def all_9_boards():
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
    i = 0
    while i < len(all_boards):
        for n in range(3):
            (r1, r2, r3) = all_boards[i][n], all_boards[i + 1][n], all_boards[i + 2][n]
            (r1, r2, r3) = [" ".join(str(element) for element in string) 
                                             for string in (r1, r2, r3)]
            print("{:^8s}{:^8s}{:^8s}".format(r1, r2, r3))
        i += 3
        print()

def nums_in_rows_and_cols(*args):
    assert len(args) == 9, "all 9 boards must be present!"
    nums_all_boards_rows = []
    a = 0
    while a < len(args):
        for i in range(3):
            nums_in_rows = args[a][i] + args[a + 1][i] + args[a + 2][i]
            nums_all_boards_rows.append(nums_in_rows)
        a += 3
    nums_all_boards_cols = [[x[i] for x in nums_all_boards_rows] 
                      for i in range(len(nums_all_boards_rows))]
    return (nums_all_boards_rows, nums_all_boards_cols)

def compute_coordinates(i, y):
    row = i if (i < 3) else i - 3 if (3 <= i <= 5) else i - 6
    col = y if (y < 3) else y - 3 if (3 <= y <= 5) else y - 6
    if i < 3:
        boardnum = 0 if (y < 3) else 1 if (3 <= y <= 5) else 2
    elif 3 <= i <= 5:
        boardnum = 3 if (y < 3) else 4 if (3 <= y <= 5) else 5
    elif 5 < i:
        boardnum = 6 if (y < 3) else 7 if (3 <= y <= 5) else 8
    return (boardnum, row, col)

def check_nums_in_board(board_i):
    remove_chars = {c for c in string.punctuation + string.whitespace}
    taken_numbers_board = {int(x) for row in board_i for x in str(board_i) 
                                 if x not in remove_chars and int(x) != 0}
    return taken_numbers_board

def fill_empty(changed=None):
    all_boards = all_9_boards() if changed is None else changed
    all_rows, all_cols = nums_in_rows_and_cols(*all_boards)
    for i in range(len(all_rows)):
        for y, number in enumerate(all_rows[i], start=0):
            if number == 0:
                boardnum, row, col = compute_coordinates(i, y)
                taken_numbers_board = check_nums_in_board(all_boards[boardnum])
                taken_numbers = ({x for x in all_rows[i] if x != 0} | 
                                 {x for x in all_cols[y] if x != 0} |
                                 taken_numbers_board)
                
                aval_numbers = set(range(1, 10)) - taken_numbers
                if len(aval_numbers) == 1:
                    print(" inserted number = {}".format(list(aval_numbers)[0]))
                    print(" board number = {}".format(boardnum + 1))
                    print(" row = {} \n col = {} \n".format(row, col))
                    all_boards[boardnum][row][col] = list(aval_numbers)[0]
    return all_boards

def all_9_boards_changed(changed):
    return changed

def main():
    changed = None
    print_all(all_9_boards())
    while True:
        zeros_count = 0
        all_boards = fill_empty() if changed is None else fill_empty(changed)
        for board in all_boards:
            for row in board:
                for number in row:
                    zero_add = 1 if number == 0 else 0
                    zeros_count += zero_add
        changed = all_9_boards_changed(all_boards)
        print_all(changed)
        print("{}\n".format("*" * 23))
        if zeros_count == 0:
            break

main()
