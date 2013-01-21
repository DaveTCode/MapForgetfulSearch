
class TileScreenConverter():
    
    def __init__(self, tile_width, tile_height):
        self.tile_width = tile_width
        self.tile_height = tile_height
        
    def tile_to_screen(self, x, y, x_offset = 0, y_offset = 0):
        return self.tile_width * x + x_offset, self.tile_height * y + y_offset
        
    def screen_to_tile(self, x, y):
        return x // self.tile_width, y // self.tile_height