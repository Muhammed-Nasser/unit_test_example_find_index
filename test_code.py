import unittest
import find_index_of_element

class TestCase(unittest.TestCase):
    
    def test1_find_index(self):
        list = [1,2,5,88,77,4,6,2,3,2]
        quary = 2
        result = find_index_of_element.get_cart_index(list, quary)
        self.assertEquals(result,"2 is exists at indexs[1, 7, 9]")
        
    def test2_find_index(self):
        list = [1,2,5,88,77,4,6,2,3,2]
        quary = 77
        result = find_index_of_element.get_cart_index(list, quary)
        self.assertEquals(result,4)
        
    def test3_find_index(self):
        list = [1,2,5,88,77,4,6,2,3,2]
        quary = 0
        result = find_index_of_element.get_cart_index(list, quary)
        self.assertEquals(result,"0 not found in this list")
        
    def test4_find_index(self):
        list = []
        quary = 1
        result = find_index_of_element.get_cart_index(list, quary)
        self.assertEquals(result,"list is empty")
        
if __name__ == '__main__':
    unittest.main()
