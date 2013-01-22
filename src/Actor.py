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
            if self.goal.x is not self.x or self.goal.y is not self.y:
                path_to_goal = self.create_path_to_goal(self.goal)
            
                if (path_to_goal is not None):
                    self.x = path_to_goal[0].x
                    self.y = path_to_goal[0].y
                else:
                    next_cell = self.explore()
                    if next_cell == None:
                        print "Stuck with no valid adjacent cells"
                    else:
                        self.x = next_cell.x
                        self.y = next_cell.y
            
            self.actor_map[self.y][self.x].last_visited = ticks
            self.update_visible_tiles(ticks)
            self.last_updated_ticks = ticks
            
    def update_visible_tiles(self, ticks): # TODO: Variable view distance?
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if self.x + x >= 0 and self.x + x < self.tile_map.width and self.y + y >= 0 and self.y + y < self.tile_map.height:
                    self.actor_map[self.y + y][self.x + x].set_type(self.tile_map[self.y + y][self.x + x], ticks)
                    
    def explore(self):
        '''
            If there isn't a direct path to the goal then the actor runs in 
            explore mode until a path exists.
            
            In explore mode the actor chooses a valid adjacent tile as follows:
            1 - Unexplored squares take precedence
            2 - Head towards the goal to break ties
            3 - Otherwise head along path travelled least recently
            4 - Head towards the goal to break ties again
        '''
        def score_tile_for_exploration(tile):
            score = tile.last_visited
            
            if not ((tile.x >= self.x and tile.x <= self.goal.x) or 
                    (tile.x >= self.goal.x and tile.x <= self.x)):
                score = score + 0.2
                
            if not ((tile.y >= self.y and tile.y <= self.goal.y) or 
                    (tile.y >= self.goal.y and tile.y <= self.y)):
                score = score + 0.2 
        
            return score
        
        adj_cells = [t for t in self.actor_map.get_adjacent_cells(self.x, self.y) if t.type == ActorMapTileType.EMPTY]
        
        if len(adj_cells) == 0:
            return None
        else:
            return min(adj_cells, key=lambda t: score_tile_for_exploration(t))
        
    
    def create_path_to_goal(self, goal):
        '''
            Uses A* algorithm to find a path from the current location to the 
            goal. If no path exists then this returns None.
        '''
        start = self.actor_map[self.y][self.x]
        open_list = []
        closed_set = set()
        
        def get_heuristic(cell):
            return (abs(goal.x - cell.x) + abs(goal.y - cell.y)) * 10
        
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