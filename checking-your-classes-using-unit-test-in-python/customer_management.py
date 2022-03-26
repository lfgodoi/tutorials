"""

Customer management

"""

import unittest

# Regular customer management class
class CustomerManagement:
    
    # Class constructor
    def __init__(self):
        self.customers = {}

    # Adding a customer
    def add_customer(self, name, car_id):
        self.customers[car_id] = name         
        
    # Removing a customer    
    def remove_customer(self, car_id):
        self.customers.pop(car_id)
       
