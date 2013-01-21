from Map import Map
from TileTypes import TileTypes

from numpy.random import random_integers as rand
 
def create_maze(width, height, complexity=.75, density=.75):
    '''
        Wikipedia algorithm for maze creation
    '''
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)

    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))

    Z = [[TileTypes.WALL if x == 0 or x == shape[1] - 1 or y == 0 or y == shape[0] - 1 else TileTypes.EMPTY for x in range(shape[1])] for y in range(shape[0])]

    for _ in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y][x] = TileTypes.WALL
        for _ in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_][x_] == TileTypes.EMPTY:
                    Z[y_][x_] = TileTypes.WALL
                    Z[y_ + (y - y_) // 2][x_ + (x - x_) // 2] = TileTypes.WALL
                    x, y = x_, y_
    
    return Map(width, height, Z)