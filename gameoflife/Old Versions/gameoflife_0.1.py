import pygame
import sys
import time
import random

rules = '''
    1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overcrowding.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'''

#Initializations:

#CONSTANTS
#-------------------
global thesize
thesize = 100
global pixelsize
pixelsize = 9
global FPS
FPS = 100
global windowsizes
windowsize = thesize*pixelsize
global generation
generation = 0
#-------------------

#Define a 2D board (List containing lists)
global board
board = [[False for x in range(thesize)] for x in range(thesize)]

#Set up colors for ease of use
BLACK = (86, 254, 184)
WHITE = (44, 44, 44)

#Set up pygame
pygame.init()
global surface
surface = pygame.display.set_mode((windowsize, windowsize)) # Define the surface for the simulation to run on
pygame.display.set_caption('Conway\'s Game of Life')
surface.fill(WHITE) # Fill the screen white
pygame.display.update()
clock = pygame.time.Clock()

#Function to round to the nearest base
def myround(x, base=5):
    return int(base * round(float(x)/base))

#Function for returning the segment that a number is in
def whichSlot(x, groupsize=pixelsize):
    return x // groupsize

#Function for returning which row and column the mouse is in
def where():
    x, y = pygame.mouse.get_pos()
    return (whichSlot(x), whichSlot(y))
#Function to find number of live neighbors
def neighbors(row, column):
    adjacents = 0

    #Horizontally adjacent
    if row > 0:
        if board[row-1][column]:
            adjacents += 1
    if column > 0:
        if board[row][column-1]:
            adjacents += 1
    if row < thesize-1:
        if board[row+1][column]:
            adjacents += 1
    if column < thesize-1:
        if board[row][column+1]:
            adjacents += 1

    #Diagonally adjacent
    if row > 0 and column > 0:
        if board[row-1][column-1]:
            adjacents += 1
    if row < thesize-1 and column < thesize-1:
        if board[row+1][column+1]:
            adjacents += 1
    if row > 0 and column < thesize-1:
        if board[row-1][column+1]:
            adjacents += 1
    if row < thesize-1 and column > 0:
        if board[row+1][column-1]:
            adjacents += 1

    #Return the final count (0-8)
    return adjacents

#Turn a space of the grid on
def giveLife(ro, col):
    topleft = [ro*pixelsize, col*pixelsize]
    topright = [topleft[0]+pixelsize, topleft[1]]
    botleft = [topleft[0], topleft[1]+pixelsize]
    botright = [topleft[0]+pixelsize, topleft[1]+pixelsize] 
    pygame.draw.polygon(surface, BLACK, [topleft, topright, botright, botleft])

#Turn a space of the grid off
def killRuthlessly(ro, col):
    topleft = [ro*pixelsize, col*pixelsize]
    topright = [topleft[0]+pixelsize, topleft[1]]
    botleft = [topleft[0], topleft[1]+pixelsize]
    botright = [topleft[0]+pixelsize, topleft[1]+pixelsize] 
    pygame.draw.polygon(surface, WHITE, [topleft, topright, botright, botleft])





#Main loop
run = False
while 1:
    #Draw the board as rectangles
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:
                giveLife(r, c)
            if not board[r][c]:
                killRuthlessly(r, c)

    #Process Events            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break;
            if event.key == pygame.K_RETURN:
                run = not run
            if event.key == pygame.K_c:
                generation = 0
                board = [[False for x in range(thesize)] for x in range(thesize)]

            if event.key == pygame.K_r:
                generation = 0
                possibilities = [False, False, True]
                for r in range(thesize):
                    for c in range(thesize):
                        board[r][c] = random.choice(possibilities)


    #RULES
    if run:
        tempboard = [[False for x in range(thesize)] for x in range(thesize)]
        for r in range(len(board)):
            for c in range(len(board)):
                neighborcount = neighbors(r, c)
                if board[r][c]: #any live cell
                    if neighborcount < 2:
                        tempboard[r][c] = False #dies
                    if neighborcount > 3: #With more than three live neighbors
                        tempboard[r][c] = False #dies
                    if neighborcount == 2 or neighborcount == 3:
                        tempboard[r][c] = True #lives on to the next generation 
                elif not board[r][c]: #any dead cell
                    if neighborcount == 3: #with exactly three live neighbors
                        tempboard[r][c] = True #becomes a live cell
        board = tempboard
        generation += 1

    presses = pygame.mouse.get_pressed()
    if presses[0]:
        putx, puty = where()
        board[putx][puty] = True
        if not run:
            generation = 0
    if presses[2]:
        putx, puty = where()
        board[putx][puty] = False
        if not run:
            generation = 0

    if run:
        clock.tick(FPS)

    pygame.display.flip()
