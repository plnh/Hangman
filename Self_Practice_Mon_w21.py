# Conway's Game of Life
"""
A filled-in square will be “alive” and an
empty square will be “dead.” If a living square has two or three living neighbors, it continues to live on the next step. If a dead square has exactly three
living neighbors, it comes alive on the next step. Every other square dies or remains dead on the next step. 
"""

import random, time, copy
def Conway(WIDTH = 60, HEIGHT= 30):
   

    nextCells = []
    for x in range(WIDTH):
        column = []
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#')
            else:
                column.append('_')
        nextCells.append(column)
    
    while True:
        print('\n\n\n\n\n')
        currentCells = copy.deepcopy(nextCells)
        
        #print on screen
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(currentCells[x][y], end='')
            print()
    
        #calculate next step cells
        for x in range(WIDTH): 
            #get neighbors' coordinate
            for y in range(HEIGHT):
                leftCoord = ( x- 1) % WIDTH # either x -1 or 0 if x == width
                rightCoord = (x+ 1) % WIDTH
                aboveCoord = (y- 1) % HEIGHT
                belowCoord = (y+ 1) % HEIGHT
            # count number of living cells
            numNeighbors = 0 
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
                
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '_' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = '_'
    time.sleep(1)

# Comma Code
"""
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'
"""

def commaCode(x):
    result = ''
    if len(x) == 0:
        result = ''
    elif len(x) == 1:
        result = x[0]
    else:
        for i in range(len(x) -1):
            result += x[i] + ', '
        result += 'and ' + x[-1]
    
    return result

# Coin Flip Streaks
"""
Write a program to find out how often a streak of six heads or a streak
of six tails comes up in a randomly generated list of heads and tails. Your
program breaks up the experiment into two parts: the first part generates
a list of randomly selected 'heads' and 'tails' values, and the second part
checks if there is a streak in it. Put all of this code in a loop that repeats the
experiment 10,000 times so we can find out what percentage of the coin
flips contains a streak of six heads or tails in a row. As a hint, the function
call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value
the other 50% of the time.
"""
import random
def coinFlip(number_of_round = 10000):
    
    coin_flip = []
    for i in range(number_of_round):
        if random.randint(0, 1) == 0:
                coin_flip.append('H')
        else:
                coin_flip.append('T')
    print(coin_flip)
    number_of_streaks = 0
    count = 0
    check = coin_flip[0]           
    for i in range(len(coin_flip)):
        temp = coin_flip[i]
        if temp == check:
            count += 1
        else:
            check = temp
            count = 0
        if count == 6:
            number_of_streaks += 1
            count = 0
                
    return number_of_streaks

# Character Picture Grid
"""
Say you have a list of lists where each value in the inner lists is a one-character
string, like this:
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
Think of grid[x][y] as being the character at the x- and y-coordinates
of a “picture” drawn with text characters. The (0, 0) origin is in the upperleft corner, the x-coordinates increase going right, and the y-coordinates
increase going down.
Copy the previous grid value, and write code that uses it to print
the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""
from typing import List
def drawGrid(grid: list):
    WIDTH = len(grid[0])
    HEIGHT = len(grid)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(grid[y][x], end='')
        print()
            
            
