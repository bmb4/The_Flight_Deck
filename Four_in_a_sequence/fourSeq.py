import numpy as np
import pygame
import math

# RBG colors
YELLOW = (255,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
CERULEAN = (42,82,190)

# pixel sizes for board and checkers
SQUARE = 100 # 100 pixels
RADIUS = 45

# this function simply creates the game board
# it is only called once in main before the game begins
def create_board():
    board = np.zeros((6,7))
    return board

# this function displays the gameboard in the pygame screen
# it draws the initial board as a large yellow rectange
# and then it will make the circles white if no checker has been placed there
# the cirlces will be black for player1 and red for player2
# then a fresh blue rectangle is drawn at the top
# a call to pygame.display.update is required to update the changes
def display_board(screen: pygame.surface, board: np.ndarray):
    for _col in range(7):
        for _row in range(6):
            pygame.draw.rect(screen, YELLOW, (_col*SQUARE, _row*SQUARE+SQUARE, SQUARE, SQUARE))
            if board[_row][_col] == 0:
                pygame.draw.circle(screen, WHITE, (int(_col*SQUARE+SQUARE/2), int(_row*SQUARE+SQUARE+SQUARE/2)),RADIUS)
            elif board[_row][_col] == 1:
                pygame.draw.circle(screen, BLACK, (int(_col*SQUARE+SQUARE/2), int(_row*SQUARE+SQUARE+SQUARE/2)),RADIUS)
            else:
                pygame.draw.circle(screen, RED, (int(_col*SQUARE+SQUARE/2), int(_row*SQUARE+SQUARE+SQUARE/2)),RADIUS)
    pygame.draw.rect(screen, CERULEAN, (0, 0, SQUARE*7, SQUARE))
    pygame.display.update()

# this function requests and returns the user input
# it was implemented here instead of just done in main
# because it can allow for certain changed to be made
# if more is required of this function
def playerInput(turn: int, column: int):
    return int(math.floor(column/SQUARE))

# this function finds the first open row in the requested column
# and inserts the player number into the first open slot
# if the requested column is full, it alerts the user
# and returns false, otherwise it returns true
def dropPiece(player: int, column: int, board: np.ndarray):
    if board[5][column] == 0:
        openRow = 0
        while openRow < 6:
            if board[openRow][column] == 0:
                board[openRow][column] = player
                return True
            else:  openRow += 1
    else:
        return False

# this function stops the audio which is currently being played
# it then plays the touchdown song from Tecmo Super Bowl (NES)
# but since the game is completed and the program wants to exit
# we make a while loop which will result in us only
# exiting this function when the mixer is no longer busy
# without the loop, the game will exit and this amazing
# song of sweet victory would not be heard
def chickenDinner():
    pygame.mixer.stop()
    win = pygame.mixer.Sound("sounds/win.ogg")
    win.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(10)
        pygame.event.poll()

# This function is called after each player drops a checker
# although it is not necessary for the first several moves
#
def winCheck(player: int, board: np.ndarray):

    # check for horizontal wins
    # simply done by going through each row
    for _rowCheck in range(0,6):
        count = 0
        for _column in range(0,7):
            if board[_rowCheck][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    # check for vertical wins
    # simply done by going through each column
    for _columnCheck in range(0,7):
        count = 0
        for _row in range(0,6):
            if board[_row][_columnCheck] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    # negative sloping diagonals
    # first we check all cases which begin in column 0
    # these can only be in rows 3 to 5
    # note these numbers are the array indexes
    for row in range(3,6):
        count = 0
        for _row, _column in zip(range(row, -1, -1), range(0, row + 1)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    # these negative sloping diagonals
    # begin in column one up to column 3
    # for each beginning column
    # we check the rows in the range (-2) + column
    # these are the "upper half" of the board
    for column in range(1,4):
        count = 0
        for _row, _column in zip(range(5, (-2) + column, -1), range(column, 7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    # check positive sloping diagonals
    # done in a similar manner as above
    for row in range (0, 2):
        count = 0
        for _row, _column in zip(range(row, 6), range(0, 7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    for column in range (1,4):
        count = 0
        for _row, _column in zip(range(0, 6), range(column ,7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    return False





