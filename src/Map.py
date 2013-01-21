from TileTypes import *

class Map():
    
    def __init__(self, width, height, tiles = None):
        self.width = width
        self.height = height
        if tiles is None:
            self.tiles = [[TileTypes.EMPTY] * width for _ in xrange(height)]
        else:
            self.tiles = tiles
        
    def set_row(self, row_ix, new_row):
        self.tiles[row_ix] = new_row
        
    def __getitem__(self, items):
        return self.tiles[items] 