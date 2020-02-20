from linear_search import linear_search
import unittest
# test to test codes
class TestLinearSearch(unittest.TestCase):
    def test_linear_search1(self):
        self.assertEqual(linear_search([5,7,8,9,2],7),1)
    
    def test_linear_search2(self):
        self.assertEqual(linear_search([5,7,8,9,2],17),-1)
if __name__ == "__main__":
    unittest.main()