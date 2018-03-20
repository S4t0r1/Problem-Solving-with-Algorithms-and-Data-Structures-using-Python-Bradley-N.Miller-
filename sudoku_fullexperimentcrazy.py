import math, string

def build_gameboard():
    board = [[0 for e in range(3)] for i in range(3)]
    return board

def extract_data():
    data = {1 : "116121222",
            2 : "013127206",
            3 : "104129218227",
            4 : "015128202",
            5 : "002105121224",
            6 : "028103215",
            7 : "004012109126",
            8 : "026103211",
            9 : "008107114"}
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


def all_sets(cell_coordinates, find_adj_row=None, find_adj_col=None):
    sets_by_adj_rows, sets_by_adj_cols = {}, {}
    for batch, value in cell_coordinates.items():
        aval_numbers, adj_row, adj_col = value
        if adj_row == find_adj_row and find_adj_row is not None:
            sets_by_adj_rows[batch] = aval_numbers
        if adj_col == find_adj_col and find_adj_col is not None:
            sets_by_adj_cols[batch] = aval_numbers
    return (sets_by_adj_rows, sets_by_adj_cols)
    
        

def check_nums_in_board(board_i):
    remove_chars = {c for c in string.punctuation + string.whitespace}
    taken_numbers_board = {int(x) for row in board_i for x in str(board_i) 
                                 if x not in remove_chars and int(x) != 0}
    return taken_numbers_board


def cell_walk(*args):
    cell_coordinates = {}
    all_adj_rows, all_adj_cols = nums_in_rows_and_cols(*args)
    for boardnum, board_n in enumerate(args):
        for rownum, row in enumerate(board_n):
            for colnum, cell in enumerate(row):
                if cell == 0:
                    taken_numbers_in_board = check_nums_in_board(args[boardnum])
                    adj_row, adj_col = calc_adj_rows_cols(boardnum, rownum, colnum, len(args))
                    taken_numbers = ({x for x in all_adj_rows[adj_row] if x != 0} | 
                                     {x for x in all_adj_cols[adj_col] if x != 0} |
                                                             taken_numbers_in_board)
                    aval_numbers = set(range(1, 10)) - taken_numbers
                    key = "".join(str(x) for x in (boardnum, rownum, colnum))
                    cell_coordinates[key] = aval_numbers, adj_row, adj_col
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
    all_free_cells = cell_walk(*all_boards)
    for key, value in all_free_cells.items():
        boardnum, row, col = tuple(int(x) for x in key)
        aval_numbers, adj_row, adj_col = value
        
        print("aval =", aval_numbers, "coordinates=", adj_row, adj_col)
        
        if len(aval_numbers) == 1:
            print(" inserted number = {}".format(list(aval_numbers)[0]))
            print(" board number = {}".format(boardnum + 1))
            print(" row = {} \n col = {} \n".format(row, col))
            all_boards[boardnum][row][col] = list(aval_numbers)[0]
            return all_boards
        
        if len(aval_numbers) == 2:
            print(adj_col)
            adj_row_sets, adj_col_sets = all_sets(all_free_cells, find_adj_col=adj_col)
            for batch, set_ in adj_col_sets.items():
                boardnum, row, col = tuple(int(x) for x in batch)
                if aval_numbers == set_ and list(adj_col_sets.values()).count(set_) > 1:
                    print("DUPLICATE =", aval_numbers)
                    new_sets = manage_sets(aval_numbers, sets_adj_cols=adj_col_sets)
                    for kei, aval in new_sets.items():
                        if key == kei:
                            all_free_cells[key] = aval, adj_row, adj_col
    return all_boards

def manage_sets(aval_numbers, sets_adj_rows=None, sets_adj_cols=None):
    for set_ in sets_adj_cols.values():
        if aval_numbers.issubset(set_) and len(aval_numbers) < len(set_):
            set_ = (set_ - aval_numbers)
    return sets_adj_cols
    

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
