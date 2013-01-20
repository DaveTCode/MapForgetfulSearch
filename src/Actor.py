
class Actor():
    
    TICK_SPEED = 1000 
    
    def __init__(self, tile_map, created_ticks):
        self.tile_map = tile_map
        self.last_updated_ticks = created_ticks
        self.x = 0
        self.y = 0
        self._find_initial_position()
        
    def _find_initial_position(self):
        self.x = 16 # TODO - Better way of finding random free spot in map
        self.y = 16
        
    def update(self, ticks):
        if (ticks - self.last_updated_ticks) > Actor.TICK_SPEED:
            self.last_updated_ticks = ticks
            pass