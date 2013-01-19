class TileTypes:    
    
    EMPTY = 0
    WALL  = 1
    
    def __init__(self):
        pass
    
    def __getitem__(self, items):
        if items == 0 or items == "0":
            return TileTypes.EMPTY
        elif items == 1 or items == "1":
            return TileTypes.WALL
        else:
            return TileTypes.EMPTY