from TextureManager import *
from TileTypes import *

class Renderer():

    TILE_WIDTH  = 20
    TILE_HEIGHT = 20
    
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (0, 0, 0)
    
    def draw_game(self, tile_map, actor):
        self.screen.fill(self.bg_color)
        self.draw_map(tile_map)
        self.draw_actor(actor)
        
        pygame.display.flip()
        
    def draw_map(self, tile_map):
        for x in range(tile_map.width):
            for y in range(tile_map.height):
                self.draw_tile(x * Renderer.TILE_WIDTH, y * Renderer.TILE_HEIGHT, tile_map[y][x])
                
    def draw_tile(self, x, y, tile_type):
        if (tile_type == TileTypes.WALL):
            self.screen.blit(TextureManager.WALL_TEXTURE, (x, y))
            
    def draw_actor(self, actor):
        self.screen.blit(TextureManager.ACTOR_TEXTURE, (actor.x * Renderer.TILE_WIDTH, actor.y * Renderer.TILE_HEIGHT))