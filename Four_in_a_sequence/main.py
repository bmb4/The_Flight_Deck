import numpy as np
import fourSeq
import pygame
import sys
import random

game_over = False
turn = 0
column = 0
fullColumns = [0,0,0,0,0,0,0]
# the width and height of each column/row
width = 700
height = 700
size = (width, height)
gameplaySongSelectionList = ["sounds/play.ogg", "sounds/play2.ogg", "sounds/play3.ogg", "sounds/play4.ogg", "sounds/play5.ogg", "sounds/play6.ogg", "sounds/play7.ogg"]

if __name__ == '__main__':

    # initialize the board as an array, pygame, and the sound
    board = fourSeq.create_board()
    pygame.init()
    pygame.mixer.init()

    # initialize the screen and display it
    screen = pygame.display.set_mode(size)
    fourSeq.display_board(screen, board)

    # randomly select amazing gameplay music
    song = random.choice(gameplaySongSelectionList)
    play = pygame.mixer.Sound(song)
    play.play()

    while not game_over:

        # pyGame is event based
        # we handle different events and dictate the programs response
        # in all games we should handle the quitting first so the program
        # can successfully exit in that scenario
        # this is why we imported sys
        for event in pygame.event.get():
            # handle quit with system exit
            if event.type == pygame.QUIT:
                sys.exit()
            # all mouse motions results in the next chip moving
            if event.type == pygame.MOUSEMOTION:
                # draw the fresh rectangle or the position from last MOUSEMOTION
                # will still be displayed, resulting in a "trail" of red/black
                pygame.draw.rect(screen, fourSeq.CERULEAN, (0,0,width,fourSeq.SQUARE))
                x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, fourSeq.BLACK, (x,50),fourSeq.RADIUS)
                else:
                    pygame.draw.circle(screen, fourSeq.RED, (x, 50), fourSeq.RADIUS)
                # we must always update the display when changes are made
                pygame.display.update()
            # clicking down on the mouse results in the piece being dropped
            if event.type == pygame.MOUSEBUTTONDOWN:
                # need recordings for dropping a chip in each row
                dropFX = pygame.mixer.Sound("sounds/drop.ogg")
                dropFX.play()
                pygame.draw.rect(screen, fourSeq.CERULEAN, (0, 0, width, fourSeq.SQUARE))
                dropHere = event.pos[0]
                # Ask for player1 input
                if turn == 0:
                    column = fourSeq.playerInput(turn, dropHere)
                    # make sure the column falls within correct range
                    if column in range(0, 7):
                        if fourSeq.dropPiece(turn + 1, column, board):
                            print(np.flip(board, 0))
                            fourSeq.display_board(screen, np.flip(board,0))
                            if fourSeq.winCheck(1, board):
                                print(f"player{turn + 1} Wins!!!!!")
                                fourSeq.chickenDinner()
                                game_over = True
                            # if the 5th row of the selected column is non-zero
                            # then we know that row must be full
                            # and we can check if all rows are full
                            # which results in a draw
                            if board[5][column] != 0:
                                fullColumns[column] = column
                            if fullColumns == [0,1,2,3,4,5,6]:
                                print("DRAW!!!!!")
                                game_over = True
                            turn += 1
                        # if dropPiece returned false, the player attempted to
                        # drop their piece in a full column
                        else:
                            print(f"player{turn + 1} you placed the piece in a full column, try again")
                    else:
                        print(f"player{turn + 1} you chose an invalid column to place your piece")
                else:
                    # Ask for player2 input
                    # same procedure as above
                    column = fourSeq.playerInput(turn, dropHere)
                    if column in range(0, 7):
                        if fourSeq.dropPiece(turn + 1, column, board):
                            print(np.flip(board, 0))
                            fourSeq.display_board(screen, np.flip(board,0))
                            if fourSeq.winCheck(2, board):
                                print(f"player{turn + 1} Wins!!!!!")
                                fourSeq.chickenDinner()
                                game_over = True
                            if board[5][column] != 0:
                                fullColumns[column] = column
                            if fullColumns == [0,1,2,3,4,5,6]:
                                print("DRAW!!!!!")
                                game_over = True
                            turn = 0
                        else:
                            print(f"player{turn + 1} you placed the piece in a full column, try again")
                    else:
                        print(f"player{turn + 1} you chose an invalid column to place your piece")







