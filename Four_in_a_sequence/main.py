import numpy as np
import fourSeq
import pygame
import sys
import random

game_over = False
turn = 0
column = 0
fullColumns = [0,0,0,0,0,0,0]
gameplaySongSelectionList = ["sounds/play.mp3", "sounds/play2.mp3", "sounds/play3.mp3", "sounds/play4.mp3", "sounds/play5.mp3", "sounds/play6.mp3", "sounds/play7.mp3"]

if __name__ == '__main__':
    board = fourSeq.create_board()
    pygame.init()
    pygame.mixer.init()
    width = 700 # this is for 7 columns, each with a width of 100 pixels
    height = 700 # this is for 6 rows, each with a width of 100 pixels plus an additional row
    size = (width, height)
    screen = pygame.display.set_mode(size)
    fourSeq.display_board(screen, board)
    song = random.choice(gameplaySongSelectionList)
    play = pygame.mixer.Sound(song)
    play.play()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, fourSeq.CERULEAN, (0,0,width,fourSeq.SQUARE))
                x = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, fourSeq.BLACK, (x,50),fourSeq.RADIUS)
                else:
                    pygame.draw.circle(screen, fourSeq.RED, (x, 50), fourSeq.RADIUS)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                dropFX = pygame.mixer.Sound("sounds/drop.mp3")
                dropFX.play()
                pygame.draw.rect(screen, fourSeq.CERULEAN, (0, 0, width, fourSeq.SQUARE))
                dropHere = event.pos[0]
                # Ask for player1 input
                if turn == 0:
                    column = fourSeq.playerInput(turn, dropHere)
                    # make sure the column falls within correct range
                    # although programmers start counting at zero
                    # most of our users will start at one
                    if column in range(1, 8):
                        if fourSeq.dropPiece(turn + 1, column, board):
                            print(np.flip(board, 0))
                            fourSeq.display_board(screen, np.flip(board,0))
                            if fourSeq.winCheck(1, board):
                                print(f"player{turn + 1} Wins!!!!!")
                                fourSeq.chickenDinner()
                                game_over = True
                            if board[5][column - 1] != 0:
                                fullColumns[column - 1] = column
                            if fullColumns == [1, 2, 3, 4, 5, 6, 7]:
                                print("DRAW!!!!!")
                                game_over = True
                            turn += 1
                    else:
                        print(f"player{turn + 1} you chose an invalid column to place your piece")
                else:
                    # Ask for player2 input
                    column = fourSeq.playerInput(turn, dropHere)
                    # make sure the column falls within correct range
                    # although programmers start counting at zero
                    # most of our users will start at one
                    if column in range(1, 8):
                        if fourSeq.dropPiece(turn + 1, column, board):
                            print(np.flip(board, 0))
                            fourSeq.display_board(screen, np.flip(board,0))
                            if fourSeq.winCheck(2, board):
                                print(f"player{turn + 1} Wins!!!!!")
                                fourSeq.chickenDinner()
                                game_over = True
                            if board[5][column - 1] != 0:
                                fullColumns[column - 1] = column
                            if fullColumns == [1, 2, 3, 4, 5, 6, 7]:
                                print("DRAW!!!!!")
                                game_over = True
                            turn = 0
                    else:
                        print(f"player{turn + 1} you chose an invalid column to place your piece")







