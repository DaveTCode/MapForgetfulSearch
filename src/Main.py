from Map import Map
from MapLoader import MapLoader
import pygame
from Renderer import Renderer
import sys

class Game():
    
    def __init__(self):
        self.renderer = None
        self.clock = None

    def setup_game(self):
        pygame.init()
        pygame.display.set_caption("Map Search Test - David Tyler (2013)")
        screen = pygame.display.set_mode((640, 480)) #TODO: Config options
        
        self.renderer = Renderer(screen)
        self.clock = pygame.time.Clock()
        self.tile_map = MapLoader().loadMap("../res/maps/map.txt")

    def run_game(self):
        if (self.renderer != None and self.clock != None):
            while True:
                time_passed = self.clock.tick(30)
            
                # TODO: Moves event handling
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit_game()
            
#                update_objects()
            
                self.renderer.draw_game(self.tile_map)
            
    def exit_game(self, rc = 0):
        pygame.quit()
        sys.exit(rc)

if __name__ == "__main__":
    game = Game()
    game.setup_game()
    game.run_game()