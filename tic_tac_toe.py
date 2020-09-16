# I plan to reset the board on every move
# I'll try that with system('clear')
from os import system

# Game Board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]

# Condition for later
game_still_going = True

# Who won
winner = None

# Whos turn is it?
current_player = 'X'


# display board function
def display_board():
    # printing board array elements together with the lines
    # which are going to represent the board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# flipping from player to player
def flip_player():
    global current_player

    # if x plays
    if current_player == "X":
        # make o play
        current_player = "O"

    # if o plays
    elif current_player == "O":
        # make x play
        current_player = "X"


# Play a game
def play_game():

    # display the board
    display_board()

    # while the game is still goning
    while game_still_going:

        # handle turns
        handle_turn(current_player)

        # Check if game has ended
        check_for_game_over()
        check_for_draw()

        # Flip to the other player
        flip_player()

    # When game ends
    if winner == "X" or winner == "O":
        # print who won
        print(winner + " won.")

    # If there is no winner
    elif winner == None:
        # It's a tie
        print("Tie.")


# handling turns
def handle_turn(player):
    
    # If x is on the move, num var is 1
    if current_player == 'X': num = 1
    # else num bar is 2
    else: num = 2

    # Trazimo ulaz od korisnika
    position = input("Player", num, "[", current_player, "] plays\nChoose a position from 1 to 9: ")

    # Varijabla koju koristimo kasnije
    # u proveravanju ispravnosti unosa
    valid = False

    # dok god je unos los, trazimo input iznova
    while not valid:
        
        # u ovom bloku proverava se da li mesto postoji
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose a position from 1 to 9: ")

        # da bi unos uporedili sa nasom listom
        # pretvaramo string iz unosa u ceo broj
        # i zbog indeksa oduzimamo jedan
        position = int(position) - 1

        # U ovom bloku proverava se da li je mesto slobodno
        if board[position] == "-":
            valid = True
        else:
            print("Already Taken. Try another one... ")

    # kada je valid = true nastavljamo dalje
    board[position] = player
    display_board()


# checking for game end
def check_for_game_over():
    check_for_win()
    check_for_draw()


# checking if someone won
def check_for_win():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()


    ## assigning the winner to the winner variable
    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None


def check_rows():
    global game_still_going

    # defining conditions to check the rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return
    

def check_columns():
    global game_still_going

    # defining conditions to check the columns
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]

    elif column_2:
        return board[1]

    elif column_3:
        return board[2]

    return


def check_diagonals():
    global game_still_going

    # defining conditions to check the diagonals
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[2]

    return


# checking if there is a tie
def check_for_draw():
    global game_still_going, winner

    if "-" not in board:
        game_still_going = False

# pozivamo glavnu funkciju
play_game()

