from TextureManager import *
from TileTypes import *

class Renderer():

    TILE_WIDTH  = 10
    TILE_HEIGHT = 10
    
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (0, 0, 0)
    
    def draw_game(self, tile_map):
        self.screen.fill(self.bg_color)
        self.draw_map(tile_map)
        
        pygame.display.flip()
        
    def draw_map(self, tile_map):
        for x in range(tile_map.width):
            for y in range(tile_map.height):
                self.draw_tile(x * Renderer.TILE_WIDTH, y * Renderer.TILE_HEIGHT, tile_map[y][x])
                
    def draw_tile(self, x, y, tile_type):
        if (tile_type == TileTypes.WALL):
            self.screen.blit(TextureManager.WALL_TEXTURE, (x, y))