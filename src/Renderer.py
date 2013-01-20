from ActorMap import ActorMapTileType
import pygame
from TileTypes import *

class Renderer():

    TILE_WIDTH  = 20
    TILE_HEIGHT = 20
    WALL_COLOR = (100, 100, 100)
    GRID_LINE_COLOR = (255, 255, 255)
    GOAL_COLOR = (0, 255, 0)
    ACTOR_COLOR = (255, 0, 0)
    BLANK_COLOR = (0, 0, 0)
    ACTOR_BLANK_COLOR = (50, 0, 0, 120)
    ACTOR_WALL_COLOR = (0, 50, 0, 120)
    
    def __init__(self, screen):
        self.screen = screen
    
    def draw_game(self, tile_map, actor):
        self.screen.fill(Renderer.BLANK_COLOR)
        self.draw_grid_lines(tile_map)
        self.draw_map(tile_map)
        self.draw_actor_overlay(actor)
        self.draw_goal(actor)
        self.draw_actor(actor)
        
        pygame.display.flip()
        
    def draw_grid_lines(self, tile_map):
        for x in range(tile_map.width):
            pygame.draw.line(self.screen, 
                             Renderer.GRID_LINE_COLOR, 
                             (x * Renderer.TILE_WIDTH, 0), 
                             (x * Renderer.TILE_WIDTH, tile_map.height * Renderer.TILE_HEIGHT))
            
        for y in range(tile_map.height):
            pygame.draw.line(self.screen, 
                             Renderer.GRID_LINE_COLOR, 
                             (0, y * Renderer.TILE_HEIGHT), 
                             (tile_map.width * Renderer.TILE_WIDTH, y * Renderer.TILE_HEIGHT))
    
    def draw_map(self, tile_map):
        for x in range(tile_map.width):
            for y in range(tile_map.height):
                self.draw_tile(x, y, tile_map[y][x])
                
    def draw_tile(self, x, y, tile_type):
        if (tile_type == TileTypes.WALL):
            self._draw_colored_tile(Renderer.WALL_COLOR, x, y)
            
    def draw_actor(self, actor):
        self._draw_colored_tile(Renderer.ACTOR_COLOR, actor.x, actor.y)
        
    def draw_goal(self, actor):
        self._draw_colored_tile(Renderer.GOAL_COLOR, actor.goal.x, actor.goal.y)
        
    def draw_actor_overlay(self, actor):
        for x in range(actor.actor_map.width):
            for y in range(actor.actor_map.height):
                color = None
                if actor.actor_map[y][x].type == ActorMapTileType.EMPTY:
                    color = Renderer.ACTOR_BLANK_COLOR
                elif actor.actor_map[y][x].type == ActorMapTileType.WALL:
                    color = Renderer.ACTOR_WALL_COLOR
                    
                if color != None:
                    self._draw_colored_tile(color, x, y)
        
    def _draw_colored_tile(self, color, tile_x, tile_y):
        self.screen.fill(color, pygame.Rect((tile_x * Renderer.TILE_WIDTH) + 1, 
                                            (tile_y * Renderer.TILE_HEIGHT) + 1,
                                            Renderer.TILE_WIDTH - 2,
                                            Renderer.TILE_HEIGHT - 2))
        