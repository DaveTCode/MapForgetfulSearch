
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