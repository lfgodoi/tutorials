"""

Customer Management Test

"""

import unittest
from customer_management import CustomerManagement

# Test customer management class
class TestCustomerManagement(unittest.TestCase):
    
    # Case 1: adding a customer
    def test_add_customer(self):
        customer_management = CustomerManagement()
        customer_management.add_customer("Leonardo Franco", "ABC-1234")

    # Case 2: removing a customer
    def test_remove_customer(self):
        customer_management = CustomerManagement()
        customer_management.add_customer("Leonardo Franco", "ABC-1234")
        customer_management.remove_customer("ABC-1234")
        
# Running the test
if __name__ == "__main__":
    unittest.main()         
