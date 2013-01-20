from ActorMap import ActorMap, ActorMapTileType
import heapq

class Actor():
    
    TICK_SPEED = 1000
    
    def __init__(self, tile_map, created_ticks):
        self.tile_map = tile_map
        self.actor_map = ActorMap(tile_map)
        self.last_updated_ticks = created_ticks
        self.x = 0
        self.y = 0
        self._find_initial_position() 
        self.goal = self.actor_map[22][22]        
        
    def _find_initial_position(self):
        self.x = 16 # TODO - Better way of finding random free spot in map
        self.y = 16
        
    def set_goal(self, x, y):
        self.goal = self.actor_map[y][x]
        
    def update(self, ticks):
        if (ticks - self.last_updated_ticks) > Actor.TICK_SPEED:
            self.update_visible_tiles(ticks)
            
            if self.goal.x is not self.x or self.goal.y is not self.y:
                path_to_goal = self.create_path_to_goal()
            
                if (path_to_goal is not None):
                    self.x = path_to_goal[0].x
                    self.y = path_to_goal[0].y
                else:
                    print "No path found"
            
            self.last_updated_ticks = ticks
            
    def update_visible_tiles(self, ticks): # TODO: Variable view distance?
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if self.x + x >= 0 and self.x + x < self.tile_map.width and self.y + y >= 0 and self.y + y < self.tile_map.height:
                    self.actor_map[self.y + y][self.x + x].set_type(self.tile_map[self.y + y][self.x + x], ticks)
                    
    def create_path_to_goal(self):
        '''
            Uses A* algorithm to find a path from the current location to the 
            goal. If no path exists then this returns None.
        '''
        start = self.actor_map[self.y][self.x]
        open_list = []
        closed_set = set()
        
        def get_heuristic(cell):
            return (abs(self.goal.x - cell.x) + abs(self.goal.y - cell.y)) * 10
        
        def update_cell(adj, cell):
            adj.g = cell.g + 10
            adj.h = get_heuristic(adj)
            adj.parent = cell
            adj.f = adj.g + adj.h
            
        def calc_path(cell):
            path = []
            while cell is not start:
                path.insert(0, cell)
                cell = cell.parent
                
            return path
            
        # add starting cell to open heap queue
        heapq.heappush(open_list, (start.f, start))
        while len(open_list):
            # pop cell from heap queue 
            _, cell = heapq.heappop(open_list)
            
            # add cell to closed list so we don't process it twice
            closed_set.add(cell)
            
            # if ending cell, display found path
            if cell is self.goal:
                return calc_path(cell)
            
            # get adjacent cells for cell
            adj_cells = self.actor_map.get_adjacent_cells(cell.x, cell.y)
            for c in adj_cells:
                if c.type == ActorMapTileType.EMPTY and c not in closed_set:
                    if (c.f, c) in open_list:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found for this adj
                        # cell.
                        if c.g > cell.g + 10:
                            update_cell(c, cell)
                    else:
                        update_cell(c, cell)
                        # add adj cell to open list
                        heapq.heappush(open_list, (c.f, c))
                        
        return None
