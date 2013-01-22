from Map import Map
from TileTypes import TileTypes

def create_city(width, height, 
                building_separation = 2, 
                max_building_width = 6, 
                max_building_height = 4):
    tiles = [[TileTypes.WALL if x == 0 or x == width - 1 or y == 0 or y == height - 1 else TileTypes.EMPTY for x in range(width)] for y in range(height)]
    
    return Map(width, height, tiles)