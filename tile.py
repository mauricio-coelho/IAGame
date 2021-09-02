import numpy as np

class Tile:
    """
    Constructor
    @param name - The name of the tile
    @param neightboors - The arraylist with\
    the possible neightboors of this tile\
        in the order (right, up, left, down)
    """
    def __init__(self, name, neightboors):
        self.name = name
        self.n_right = neightboors[0]
        self.n_up = neightboors[1]
        self.n_left = neightboors[2]
        self.n_down = neightboors[3]
        self.neightboors = neightboors

    # TODO use later
    # def __init__(self, name, neightboors, image):
    #     self.name = name
    #     self.n_right = neightboors[0]
    #     self.n_up = neightboors[1]
    #     self.n_left = neightboors[2]
    #     self.n_down = neightboors[3]
    #     self.neightboors = neightboors
    #     self.image = image
    
    """
    Return the array of all the neightboors
    """
    def get_neightboors():
        return self.neightboors

    def get_neightboor(direction):
        """
        Return a specific direction neightboor
        @param direction - The direction to get the neightboor of
        """
        if direction == "R":
            return self.n_right
        elif direction == "U":
            return self.n_up
        elif direction == "L":
            return self.n_left
        else: 
            return self.n_down