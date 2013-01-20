from TileTypes import *

class Map():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[TileTypes.EMPTY] * width for _ in xrange(height)]
        
    def set_row(self, row_ix, new_row):
        self.tiles[row_ix] = new_row
        
    def __getitem__(self, items):
        return self.tiles[items] 