import math, string

def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board

def extract_data():
    data = {1 : "013024118",
            2 : "026212224",
            3 : "114203218225",
            4 : "021123",
            5 : "014027102111129205216",
            6 : "108201",
            7 : "006017028112",
            8 : "001013204",
            9 : "111206215"}
    assert len(data.keys()) == 9, "data must comply with 9 boards"
    return data

def all_9_boards():
    all_boards = [build_gameboard() for board in range(9)]
    data = extract_data() 
    for key, value in data.items():
        assert len(value) % 3 == 0, "coordinates info must be in x,y,v sequence"
        boardnum = key - 1
        value = [tuple(int(x) for x in (value[i], value[i + 1], value[i + 2])) 
                                             for i in range(0, len(value), 3)]
        for coordinate_info in value:
            x, y, v = coordinate_info
            all_boards[boardnum][x][y] = v
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
    adjacent_boards_rows = []
    a = 0
    while a < len(args):
        for i in range(3):
            nums_in_rows_line = args[a][i] + args[a + 1][i] + args[a + 2][i]
            adjacent_boards_rows.append(nums_in_rows_line)
        a += 3
    adjacent_boards_cols = [[x[i] for x in adjacent_boards_rows] 
                      for i in range(len(adjacent_boards_rows))]
    return (adjacent_boards_rows, adjacent_boards_cols)

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
