from Map import Map
from TileTypes import *

class MapLoader():
    
    def loadMap(self, filename):        
        with open(filename, "r") as map_file:
            parts = map_file.readline().split(",")
            width = int(parts[0])
            height = int(parts[1])
            
            m = Map(width, height)
            r = 0
            for line in map_file:
                row = [TileTypes()[t] for t in line.strip('\n').split(",")]
                m.set_row(r, row)
                r = r + 1

        return m