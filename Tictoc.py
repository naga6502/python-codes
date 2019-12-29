import re
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

current_player = 'X'

game_still_going = True

winner = None


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2] + '\n'+ board[3]+" | "+board[4]+" | "+board[5] +'\n' + board[6]+" | "+board[7]+" | "+board[8])


display_board()


def play_game():

    while game_still_going:
        handle_input(current_player)
        check_if_game_over()
        filp_player()

    if winner == 'X' or winner == 'O':
        print(winner," won.")
    elif winner == None:
        print("Tie.")


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def filp_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]


def check_columns():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]


def check_for_winner():
    global winner

    row_winner = check_rows()
    col_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_for_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


def handle_input(player):
    print(player, '\'s turn')
    position = input("choose number from 1-9:")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose number from 1-9:")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there.Go again")
    board[position] = player
    display_board()


play_game()
