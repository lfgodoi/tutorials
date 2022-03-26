"""

Parking Lot Test

"""

import unittest
from parking_lot import ParkingLot

# Test class
class TestParkingLot(unittest.TestCase):    

    # Case 1: trying to occupy 51 spaces when just 50 are available
    def test_occupy_more_than_available_spaces(self):
        parking_lot = ParkingLot(50)
        parking_lot.occupy_spaces(51)
        self.assertEqual(parking_lot.available_spaces, 0)

    # Case 2: trying to release a space when no one has been occupied so far
    def test_release_unoccupied_spaces(self):
        parking_lot = ParkingLot(50)
        parking_lot.release_spaces(1)
        self.assertEqual(parking_lot.available_spaces, 50)
        
    # Case 3: occupying 49 spaces when there are 50 available
    def test_normal_occupation(self):
        parking_lot = ParkingLot(50)
        parking_lot.occupy_spaces(49)
        self.assertEqual(parking_lot.available_spaces, 1)

    # Case 4: releasing 3 spaces after occupying 5
    def test_normal_release(self):
        parking_lot = ParkingLot(50)
        parking_lot.occupy_spaces(5)
        parking_lot.release_spaces(3)
        self.assertEqual(parking_lot.available_spaces, 48)
        
    # Case 5: trying to pass a non-int as the number of spaces to be occupied
    def test_occupy_spaces_type(self):
        parking_lot = ParkingLot(50)
        self.assertRaises(TypeError, parking_lot.occupy_spaces, "My string")

    # Case 6: trying to pass a non-int as the number of spaces to be released
    def test_release_spaces_type(self):
        parking_lot = ParkingLot(50)
        parking_lot.occupy_spaces(5)
        self.assertRaises(TypeError, parking_lot.release_spaces, True)

# Running the test
if __name__ == "__main__":
    unittest.main()            
    
