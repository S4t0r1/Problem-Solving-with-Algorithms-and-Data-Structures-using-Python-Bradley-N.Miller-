import math, string


def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board


def extract_data():
    data = {1 : "121208",
            2 : "106129211",
            3 : "015028219222",
            4 : "027106129",
            5 : "023208",
            6 : "103124202",
            7 : "004013207211",
            8 : "012104121",
            9 : "029108"}
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
            magic = all_boards[i][n], all_boards[i + 1][n], all_boards[i + 2][n]
            (r1, r2, r3) = [" ".join(str(element) for element in string) 
                                                    for string in magic]
            print("{:^8s}{:^8s}{:^8s}".format(r1, r2, r3))
        i += 3
        print()


def nums_in_rows_and_cols(*args):
    assert len(args) == 9, "all 9 boards must be present!"
    adjacent_boards_rows = [args[a][i] + args[a + 1][i] + args[a + 2][i] 
                      for a in range(0, len(args), 3) for i in range(3)]
    adjacent_boards_cols = [[x[i] for x in adjacent_boards_rows] 
                      for i in range(len(adjacent_boards_rows))]
    return (adjacent_boards_rows, adjacent_boards_cols)
    

def check_nums_in_board(board_i):
    remove_chars = {c for c in string.punctuation + string.whitespace}
    taken_numbers_board = {int(x) for row in board_i for x in str(board_i) 
                                 if x not in remove_chars and int(x) != 0}
    return taken_numbers_board


def create_sets(cell_coordinates, changed=None):
    all_boards = all_9_boards() if changed is None else changed
    all_adj_rows, all_adj_cols = nums_in_rows_and_cols(*all_boards)
    all_nums = set(range(1, 10))
    cell_data = {}
    for batch, adj_coordinates in cell_coordinates.items():
        boardnum = int(batch[0])
        adj_row, adj_col = adj_coordinates
        taken_nums_board = check_nums_in_board(all_boards[boardnum])
        taken_nums = ({x for x in all_adj_rows[adj_row] if x != 0} | 
                      {x for x in all_adj_cols[adj_col] if x != 0}
                                               | taken_nums_board)
        cell_set = all_nums - taken_nums
        cell_data[batch] = cell_set, adj_row, adj_col
    adj_row_sets, adj_col_sets, board_sets = {}, {}, {}
    for i in range(len(all_boards)):
        for batch, values in cell_data.items():
            boardnum = int(batch[0])
            cell_set, adj_row, adj_col = values
            if adj_row == i:
                adj_row_sets[batch] = cell_set, adj_row, adj_col
            if adj_col == i:
                adj_col_sets[batch] = cell_set, adj_row, adj_col
            if boardnum == i:
                board_sets[batch] = cell_set, adj_row, adj_col
    return cell_data, adj_row_sets, adj_col_sets, board_sets


def cell_walk(*args):
    cell_coordinates = {}
    for b_num, board_n in enumerate(args):
        for r_num, row in enumerate(board_n):
            for c_num, cell in enumerate(row):
                if cell == 0:
                    adj_row, adj_col = calc_adj_rows_cols(b_num, r_num, c_num, len(args))
                    key = "".join(str(x) for x in (b_num, r_num, c_num))
                    cell_coordinates[key] = adj_row, adj_col
    return cell_coordinates
 

def calc_adj_rows_cols(boardnum, row, col, all_boards_len):
    root = int(math.sqrt(all_boards_len))
    adj_row = (row if boardnum in {0, 1, 2} 
          else row + root if boardnum in {3, 4, 5}
          else row + (root + root))
    adj_col = (col if boardnum in {0, 3, 6}
          else col + root if boardnum in {1, 4, 7}
          else col + (root + root))
    return adj_row, adj_col


def fill_empty(changed=None):
    all_boards = all_9_boards() if changed is None else changed
    cell_coordinates = cell_walk(*all_boards)
    for key, value in cell_coordinates.items():
        boardnum, row, col = tuple(int(x) for x in key)
        cell_data, adj_row_sets, adj_col_sets, board_sets = create_sets(cell_coordinates, all_boards)
        aval_nums = cell_data[key][0]
        ars_changed, acs_changed, bs_changed = manage_sets(adj_row_sets, adj_col_sets, board_sets)
        for data in (ars_changed, acs_changed, bs_changed):
            for batch, new_value in data.items():
                boardnum, row, col = tuple(int(x) for x in batch)
                aval_numbers, adj_row, adj_col = new_value
                print(aval_numbers)
                if len(aval_numbers) == 1:
                    print(" inserted number = {}".format(list(aval_numbers)[0]))
                    print(" board number = {}".format(boardnum))
                    print(" row = {} \n col = {} \n".format(row, col))
                    all_boards[boardnum][row][col] = list(aval_numbers)[0]
                    return all_boards
    return all_boards


def manage_sets(*args):
    assert len(args) == 3, "can have only 3 set arrays (by adj_rows, adj_cols and board)"
    for arg in args[:2]:
        sets_lst = [value[0] for value in arg.values()]
        dupset = set()
        for batch, value in arg.items():
            set_, adj_row, adj_col = value
            if sets_lst.count(set_) > 1:
                dupset = set_
                continue
            if set_ != dupset:
                if dupset.issubset(set_):
                    set_ = set_ - dupset
                if dupset.issuperset(set_):
                    for num_s in set_:
                        for otherset_ in sets_lst:
                            if num_s not in otherset_:
                                magicnum = num_s
                                break
                    for num_d in dupset:
                        if num_d in set_ and num_d != magicnum:
                            set_.remove(num_d)
                
            arg[batch] = set_, adj_row, adj_col
            for item in (args[1], args[2]):
                for batch_2, value_2 in item.items():
                    if batch_2 == batch:
                        item[batch_2] = set_, adj_row, adj_col
    if args[-1]:
        sets_in_board = args[-1]
        sets_for_board_lst = [value[0] for value in sets_in_board.values()]
        candidates_count = [tuple(x)[i] for x in sets_for_board_lst for i in range(len(x))]
        sole_candidate = set()
        for candidate in candidates_count:
            if candidates_count.count(candidate) == 1:
                sole_candidate.add(candidate)
                for key, val in sets_in_board.items():
                    sett, adj_row, adj_col = val
                    if candidate in sett:
                        sets_in_board[key] = sole_candidate, adj_row, adj_col
    return args

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

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
