import random

import pygame


"""Pythonic implementation of Conway's Game of Life.

Rules:
  1. Any live cell with fewer than two live neighbours dies, as if caused
    by under-population.
  2. Any live cell with two or three live neighbours lives on to the next
    generation.
  3. Any live cell with more than three live neighbours dies, as if by
    overcrowding.
  4. Any dead cell with exactly three live neighbours becomes a live cell,
    as if by reproduction.

"""
#Initializations:

#CONSTANTS
#-------------------
FOREGROUND = pygame.Color(86, 254, 184, 255)
FPS = 30
THE_SIZE = 100
PIXEL_SIZE = 9
BACKGROUND = pygame.Color(44, 44, 44, 255)
WINDOW_SIZE = THE_SIZE*PIXEL_SIZE
#-------------------

#Define a 2D board (List containing lists)
board = [[False for _ in range(THE_SIZE)] for _ in range(THE_SIZE)]
oldboard = [row[:] for row in board]

#Set up pygame
pygame.init()
surface = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
surface.fill(BACKGROUND) # Fill the screen BACKGROUND
pygame.display.update()
clock = pygame.time.Clock()
generation = 0


def realToWorldCoordinates(inputtuple):
    """Return which row and column the real coordinates would fall in"""
    x, y = inputtuple
    return (x // PIXEL_SIZE, y // PIXEL_SIZE)


def liveNeighbors(row, column):
    """Function to find number of live neighbors"""
    adjacents = 0

    #Horizontally adjacent
    if row > 0:
        if board[row-1][column]:
            adjacents += 1
    if column > 0:
        if board[row][column-1]:
            adjacents += 1
    if row < THE_SIZE-1:
        if board[row+1][column]:
            adjacents += 1
    if column < THE_SIZE-1:
        if board[row][column+1]:
            adjacents += 1

    #Diagonally adjacent
    if row > 0 and column > 0:
        if board[row-1][column-1]:
            adjacents += 1
    if row < THE_SIZE-1 and column < THE_SIZE-1:
        if board[row+1][column+1]:
            adjacents += 1
    if row > 0 and column < THE_SIZE-1:
        if board[row-1][column+1]:
            adjacents += 1
    if row < THE_SIZE-1 and column > 0:
        if board[row+1][column-1]:
            adjacents += 1

    #Return the final count (0-8)
    return adjacents


def giveLife(ro, col):
    """Turn a space of the grid on"""
    rect = pygame.Rect(ro*PIXEL_SIZE, col*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
    pygame.draw.rect(surface, FOREGROUND, rect)


def killRuthlessly(ro, col):
    rect = pygame.Rect(ro*PIXEL_SIZE, col*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
    pygame.draw.rect(surface, BACKGROUND, rect)



#Main loop
run = False
while 1:

    #Process Events            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break;
            if event.key == pygame.K_RETURN:
                run = not run
            if event.key == pygame.K_c:
                generation = 0
                board = [[False for x in range(THE_SIZE)] for x in range(THE_SIZE)]

            if event.key == pygame.K_r:
                generation = 0
                possibilities = [False, False, True]
                for r in range(THE_SIZE):
                    for c in range(THE_SIZE):
                        board[r][c] = random.choice(possibilities)


    #RULES
    if run:
        tempboard = [[False for x in range(THE_SIZE)] for x in range(THE_SIZE)]
        for r in range(len(board)):
            for c in range(len(board)):
                neighborcount = liveNeighbors(r, c)
                if board[r][c]: #any live cell
                    if neighborcount < 2:
                        tempboard[r][c] = False #dies
                    elif neighborcount > 3: #With more than three live neighbors
                        tempboard[r][c] = False #dies
                    elif neighborcount == 2 or neighborcount == 3:
                        tempboard[r][c] = True #lives on to the next generation 
                elif not board[r][c]: #any dead cell
                    if neighborcount == 3: #with exactly three live neighbors
                        tempboard[r][c] = True #becomes a live cell
        board = tempboard
        generation += 1

    presses = pygame.mouse.get_pressed()
    if presses[0]:
        putx, puty = realToWorldCoordinates(pygame.mouse.get_pos())
        board[putx][puty] = True
        if not run:
            generation = 0
    if presses[2]:
        putx, puty = realToWorldCoordinates(pygame.mouse.get_pos())
        board[putx][puty] = False
        if not run:
            generation = 0

    #Draw the board as rectangles
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] and not oldboard[r][c]:
                giveLife(r, c)
            if not board[r][c]:
                killRuthlessly(r, c)

    if run:
        clock.tick(FPS)

    oldboard = [row[:] for row in board]

    pygame.display.flip()

