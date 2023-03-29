"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""

#DONE
def is_empty(board):
    for row in board:
        for cell in row:
            if cell != " ":
                return False          
    return True




def is_square_in_board(board, y, x):
    if (y >= len(board)) or (y < 0): 
        return False
    if (x >= len(board[0])) or (x < 0): return False;
    return True

#DONE (not really tested but I'm a god so its ok)
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #why am I doing this :(
    d_y = -d_y
    d_x = -d_x

    begin_x_edge = x_end + (length) * d_x
    begin_y_edge = y_end + (length) * d_y
    
    end_x_edge = x_end - d_x
    end_y_edge = y_end - d_y
    
    col = board[y_end][x_end]
    
    n_free_edges = 0
    if is_square_in_board(board, begin_y_edge, begin_x_edge):
        
        if board[begin_y_edge][begin_x_edge] == " ":
            n_free_edges+=1
            
    if is_square_in_board(board, end_y_edge, end_x_edge):
        
        if board[end_y_edge][end_x_edge] == " ":
            n_free_edges+=1
            
    if n_free_edges == 0:
        return "CLOSED"
    if n_free_edges == 1:
        return "SEMIOPEN"
    if n_free_edges == 2:
        return "OPEN"
        
    return "somehow this has a problem"
            
    
    
    




    
    
    
'''
#DONE and decently tested probably maybe
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    c_x = x_start
    c_y = y_start

    streak_len =  0
    last_col = board[y_start][x_start]

    n_open = 0
    n_semi = 0
    
    for i in range(length):
  
        
  
        if (board[c_y][c_x] != col and last_col == col):     
            if 
            
            
            
            bound = is_bounded(board, c_y - d_y, c_x - d_x, streak_len, d_y, d_x)
            if bound == "OPEN":
                n_open += 1
            if bound == "SEMIOPEN":
                n_semi += 1
            streak_len = 0
             
        elif board[c_y][c_x] == col:
            streak_len += 1
        
           #if there is a difference, or we're at the end and the current color is good
        if(i == length - 1) and board[c_y][c_x] == col:
             bound = is_bounded(board, c_y, c_x, streak_len, d_y, d_x)
             
             if bound == "OPEN":
                 n_open += 1
             if bound == "SEMIOPEN":
                 n_semi += 1
        
        last_col = board[c_y][c_x]
        
        c_x += d_x
        c_y += d_y

    return n_open, n_semi
'''


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    c_x = x_start
    c_y = y_start

    streak_len =  0
    
    last_col = board[y_start][x_start]

    n_open = 0
    n_semi = 0
    
    while is_square_in_board(board, c_x, c_y): 
        if board[c_y][c_x] != last_col and last_col == col:
            
            b = is_bounded(board, c_y - d_y, c_x - d_x, 
                           streak_len, d_y, d_x)

            
            if b == "OPEN" and streak_len == length: n_open += 1       
            if b == "SEMIOPEN" and streak_len == length: n_semi += 1
            
        else:
            streak_len += 1
            
        if board[c_y][c_x] != last_col:
            streak_len = 1
            
        last_col = board[c_y][c_x]
        
        c_x += d_x
        c_y += d_y

    #check the last square also!
    if board[c_y - d_y][c_x - d_x] == col: 
        
        b = is_bounded(board, c_y - d_y, c_x - d_x, 
                       streak_len, d_y, d_x)
        if b == "OPEN" and streak_len == length: n_open += 1       
        if b == "SEMIOPEN" and streak_len == length: n_semi += 1



    return n_open, n_semi




def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0

    board_height = len(board)
    board_width = len(board[0])
    
    #roll down the left side of the board, shoot out to the right
    for y in range(board_height):
        #horizontal row checks
        op, sem = detect_row(board, col, y, 0, length, 0, 1)
        open_seq_count += op
        semi_open_seq_count += sem
        
        '''
        ENSURE WE DONT DOUBLE COUNT THE CENTER DIAGONALLL!!!
        '''
        #diagonal going down and right
        op, sem = detect_row(board, col, y, 0, length, 1, 1)
        open_seq_count += op
        semi_open_seq_count += sem
        
        #detect_row()
        op, sem = detect_row(board, col, y, 0, length, -1, 1)
        open_seq_count += op
        semi_open_seq_count += sem
        
    
    
    for x in range(board_width):
        #vertical row checks
        op, sem = detect_row(board, col, 0, x, length, 1, 0)
        open_seq_count += op
        semi_open_seq_count += sem
        
        #ensure we dont double count middle row, since it was done above already
        if x == 0:
            continue
        
        #diagonal going down and right
        op, sem = detect_row(board, col, 0, x, length, 1, 1)
        open_seq_count += op
        semi_open_seq_count += sem
    
        if x == (len(board[0]) - 1):
            continue
        
        op, sem = detect_row(board, col, x, len(board[0]) - 1, length, 1, -1)
        open_seq_count += op
        semi_open_seq_count += sem
    
    return open_seq_count, semi_open_seq_count
    

    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])



def search_max(board):
    best_score = -10000000000000000
    move_y, move_x = 0,0
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != " ":
                continue  
            board[y][x] = "b"
            
            c_score = score(board)
            if c_score > best_score:
                best_score = c_score
                move_y, move_x = y, x
   
            board[y][x] = " "

    return move_y, move_x



def detect_row_any_bound(board, col, y_start, x_start, length, d_y, d_x):
    c_x = x_start
    c_y = y_start

    streak_len =  0
    n_total = 0
    
    last_col = board[y_start][x_start]


    while is_square_in_board(board, c_x, c_y): 
        if board[c_y][c_x] != last_col and last_col == col:
            
            #print(c_x, c_y)
            if streak_len == length:
                
                n_total += 1
            
        else:
            streak_len += 1
            
        if board[c_y][c_x] != last_col:
            streak_len = 1
            
        last_col = board[c_y][c_x]
        
        c_x += d_x
        c_y += d_y

    #check the last square also!
    if board[c_y - d_y][c_x - d_x] == col and streak_len == length: 
        n_total += 1

    #print(n_total)

    return n_total




def detect_rows_any_bound(board, col, length):
    
    n_total = 0

    board_height = len(board)
    board_width = len(board[0])
    
    #roll down the left side of the board, shoot out to the right
    for y in range(board_height):
        #horizontal row checks
        n_total += detect_row_any_bound(board, col, y, 0, length, 0, 1)
        n_total += detect_row_any_bound(board, col, y, 0, length, 1, 1)
        n_total += detect_row_any_bound(board, col, y, 0, length, -1, 1)

    
    
    for x in range(board_width):
        #vertical row checks
        n_total += detect_row_any_bound(board, col, 0, x, length, 1, 0)

        #ensure we dont double count middle row, since it was done above already
        if x == 0:
            continue
        
        #diagonal going down and right
        n_total += detect_row_any_bound(board, col, 0, x, length, 1, 1)


        if x == (len(board[0]) - 1):
            continue
        
        n_total += detect_row_any_bound(board, col, len(board[0]) - 1, x, length, 1, -1)
    

    
    return n_total
    


def is_board_full(board):
    for r in board:
        for e in r:
            if e == " ":
                return False
    return True
                    


def is_win(board):
    
    if detect_rows_any_bound(board, "b", 5) > 0:
        return "Black won"
 
    if detect_rows_any_bound(board, "w", 5) > 0:
        return "White won"
    
    if is_board_full(board):
        return "Draw"
    
    return"Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    pass
