from Actor import Actor
from MapLoader import MapLoader
import pygame
from pygame.locals import *
from Renderer import Renderer
import sys

class Game():
    
    def __init__(self):
        self.renderer = None
        self.clock = None

    def setup(self):
        pygame.init()
        pygame.display.set_caption("Map Search Test - David Tyler (2013)")
        pygame.event.set_allowed([QUIT, KEYDOWN])
        screen = pygame.display.set_mode((1280, 960)) #TODO: Config options
        
        self.renderer = Renderer(screen)
        self.clock = pygame.time.Clock()
        self.tile_map = MapLoader().loadMap("../res/maps/map.txt")
        self.actor = Actor(self.tile_map, pygame.time.get_ticks())

    def run(self):
        if (self.renderer != None and self.clock != None):
            while True:
                self.clock.tick(30)
            
                # TODO: Move event handling
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.exit_game()
            
                self.actor.update(pygame.time.get_ticks())
            
                self.renderer.draw_game(self.tile_map, self.actor)
            
    def exit_game(self, rc = 0):
        pygame.quit()
        sys.exit(rc)

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.run()