class ActorMap():
    
    def __init__(self, tile_map):
        self.actual_tile_map = tile_map
        self.known_tile_map = [[ActorMapTile(ActorMapTileType.UNKNOWN, -1, x, y) for x in range(tile_map.width)] for y in range(tile_map.height)]
        self.width = tile_map.width
        self.height = tile_map.height
        
    def __getitem__(self, items):
        return self.known_tile_map[items]
    
    def get_adjacent_cells(self, x, y):
        cells = []
        if x < self.width - 1:
            cells.append(self.known_tile_map[y][x + 1])
        if x > 0:
            cells.append(self.known_tile_map[y][x - 1])
        if y > 0:
            cells.append(self.known_tile_map[y - 1][x])
        if y < self.height - 1:
            cells.append(self.known_tile_map[y + 1][x])
            
        return cells
    
    def nearest_known_cell_to_goal(self, goal, radius_to_check):
        '''
            Find the tile nearest to the goal with known information.
        '''
        for radius in range(1, min([max([goal.x, self.width - goal.x, goal.y, self.height - goal.y]), 
                                   radius_to_check])):
            cellsToCheck = [self.known_tile_map[y][x] 
                            for x in range(goal.x - radius, goal.x + radius) 
                            for y in range(goal.y - radius, goal.y + radius) 
                            if (x != goal.x or y != goal.y) and 
                               x >= 0 and x < self.width and 
                               y >= 0 and y < self.height]
            
            for cell in cellsToCheck:
                if cell.last_discovered > -1:
                    return cell
        
        return None
        
class ActorMapTile():
     
    def __init__(self, tile_type, t, x, y):
        self.type = tile_type
        self.last_discovered = t
        self.last_visited = t
        self.x = x
        self.y = y
        
        # A* information - TODO: Should be separated
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0
        
    def set_type(self, tile_type, t):
        self.type = tile_type
        self.last_discovered = t
        
    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

class ActorMapTileType():
    
    UNKNOWN = -1
    EMPTY = 0
    WALL = 1