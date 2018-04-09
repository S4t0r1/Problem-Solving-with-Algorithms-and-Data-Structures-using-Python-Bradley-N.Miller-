
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


def create_sets(cell_data, numOfBoards):
    all_adj_row_sets, all_adj_col_sets, all_board_sets = [], [], []
    for i in range(numOfBoards):
        board_sets = [(key, value[0]) for key, value in cell_data.items() if int(key[0]) == i]
        all_board_sets.append(board_sets)
        adj_row_sets = [(key, value[0]) for key, value in cell_data.items() if value[1] == i]
        all_adj_row_sets.append(adj_row_sets)
        adj_col_sets = [(key, value[0]) for key, value in cell_data.items() if value[2] == i]
        all_adj_col_sets.append(adj_col_sets)
    return all_board_sets, all_adj_row_sets, all_adj_col_sets


def cell_walk(*args):
    cell_coordinates = {}
    zeroCount = 0
    all_adj_rows, all_adj_cols = nums_in_rows_and_cols(*args)
    for b_num, board_n in enumerate(args):
        for r_num, row in enumerate(board_n):
            for c_num, cell in enumerate(row):
                if cell == 0:
                    adj_row, adj_col = calc_adj_rows_cols(b_num, r_num, c_num, len(args))
                    taken_nums_board = check_nums_in_board(args[b_num])
                    taken_nums = ({x for x in all_adj_rows[adj_row] if x != 0} | 
                                  {x for x in all_adj_cols[adj_col] if x != 0}
                                                           | taken_nums_board)
                    cell_set = set(range(1, 10)) - taken_nums
                    key = "".join(str(x) for x in (b_num, r_num, c_num))
                    cell_coordinates[key] = cell_set, adj_row, adj_col
                    zeroCount += 1
    return cell_coordinates, zeroCount
 

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
    cell_data, zeroCount = cell_walk(*all_boards)
    allBoardSets, allRowSets, allColSets = create_sets(cell_data, len(all_boards))
    while zeroCount > 0:
        for key, value in cell_data.items():
            boardnum, row, col = tuple(int(x) for x in key)
            cell_set, adj_row, adj_col = value
            print(cell_set)
            if len(cell_set) == 1:
                print(" inserted number = {}".format(list(cell_set)[0]))
                print(" board number = {}".format(boardnum))
                print(" row = {} \n col = {} \n".format(row, col))
                all_boards[boardnum][row][col] = list(cell_set)[0]
                return all_boards
            else:
                cell_data = manage_sets(cell_data, allBoardSets[boardnum], 
                                 allRowSets[adj_row], allColSets[adj_col])
    return all_boards


def manage_sets(*args):
    cell_data = args[0]
    boardSets, rowSets, colSets = args[1], args[2], args[3]
    dupset, sole_candidate = set(), set()
    for setsList in (boardSets, rowSets, colSets):
        candidatesList = [tuple(x[1])[i] for x in setsList for i in range(len(x[1]))]
        candidatesKey = " ".join(x[0] + str(i) for x in setsList for i in range(len(x[1])))
        candidatesDict = {candidatesKey: candidatesList}
        for keys, candidates in candidatesDict.items():
            for index, candidate in enumerate(candidates):
                if candidates.count(candidate) == 1:
                    keys = keys.split()
                    batch = keys[index][:-1]
                    sole_candidate.add(candidate)
                    cell_data[batch] = sole_candidate, cell_data[batch][1], cell_data[batch][2]
                    return cell_data
         
        setsKeysStr = " ".join(item[0] for item in setsList)
        setsCountList = [item[1] for item in setsList]
        print(setsCountList)
        dupset = [s for s in setsCountList if setsCountList.count(s) == len(s)]
        if dupset:
            dupset = dupset[0]
            for index, cell_set_ in enumerate(setsCountList):
                batch = setsKeysStr.split()[index]
                if cell_set_ != dupset:
                    if dupset.issubset(cell_set_):
                        cell_set_ = cell_set_ - dupset
                        cell_data[batch] = cell_set_, cell_data[batch][1], cell_data[batch][2]
                        return cell_data
                    else:
                        pairNumLst = list(cell_set_) + list(dupset)
                        removenums = {num for num in pairNumLst if pairNumLst.count(num) == len(dupset)}
                        if removenums:
                            cell_set_ = cell_set_ - removenums
                            cell_data[batch] = cell_set_, cell_data[batch][1], cell_data[batch][2]
                            return cell_data
    return cell_data


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
