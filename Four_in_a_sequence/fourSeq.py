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
        print(f"player{player}, you have selected an invalid location")
        return False

def chickenDinner():
    pygame.mixer.stop()
    win = pygame.mixer.Sound("sounds/win.ogg")
    win.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(10)
        pygame.event.poll()

def winCheck(player: int, board: np.ndarray):
    # check diagonals SW to NE
    # because we need to have four in a sequence
    # on diagonals we can only count rows 1 and 2 to get four
    # from this direction, which is like the upper half
    # of a diagonal slice if looking at real connect four
    for _rowStart in range (0, 2):
        count = 0
        for _row, _column in zip(range(_rowStart,6), range(0,7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    for _colStart in range (1,4):
        count = 0
        for _row, _column in zip(range(0,6), range(_colStart,7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    #check horizontal
    for _rowCheck in range(0,6):
        count = 0
        for _column in range(0,7):
            if board[_rowCheck][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    #check vertical
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
    # we check the rows in the range (-1) + column
    # these are the "upper half" of the board
    for column in range(1,4):
        count = 0
        for _row, _column in zip(range(5, (-2) + column, -1), range(column, 7)):
            if board[_row][_column] == player:
                count += 1
                if count >= 4:
                    return True
            else: count = 0

    return False





