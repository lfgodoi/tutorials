"""

Parking Lot

"""

import unittest

# Regular class
class ParkingLot():
    
    # Class constructor
    def __init__(self, initial_spaces):
        self.available_spaces = initial_spaces
        self.total_spaces = initial_spaces
        
    # Method triggered when one or more spaces are occupied    
    def occupy_spaces(self, n_spaces):
        if type(n_spaces) != int:
            raise TypeError("Input type must be an integer")
        if self.available_spaces > n_spaces:
            self.available_spaces -= n_spaces
        else:
            self.available_spaces = 0
    
    # Method triggered when one or more spaces are released    
    def release_spaces(self, n_spaces):
        if type(n_spaces) != int:
            raise TypeError("Input type must be an integer")
        self.available_spaces += n_spaces
        if self.available_spaces > self.total_spaces:
            self.available_spaces = self.total_spaces
