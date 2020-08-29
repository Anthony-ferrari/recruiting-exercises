import unittest
from inventoryAllocator2 import inventoryAllocator


class Test_classes(unittest.TestCase):  # The class name can be whatever you want
    """
    Contains unit tests for the inventoryAllocation class
    """
    def setUp(self):
        """Sets inventoryAllocation properties for use in unit testing"""
        # trivial cases from github readME

        # 1: items split between two warehouses
        self.items1 = {'apple': 10}
        self.warehouse1 = [{ 'name': 'owd', 'inventory': { 'apple': 5} }, {'name': 'dm', 'inventory': {'apple':5}}]
        self.inventoryCheck1 = inventoryAllocator(self.items1, self.warehouse1)
        # 2: items coming from one warehouse
        self.items2 = {'apple': 1}
        self.warehouse2 = [{ 'name': 'owd', 'inventory': { 'apple': 1} }]
        self.inventoryCheck2 = inventoryAllocator(self.items2, self.warehouse2)
        # 3: not enough items from warehouses available
        self.items3 = {'apple': 1}
        self.warehouse3 = [{ 'name': 'owd', 'inventory': { 'apple': 0} }]
        self.inventoryCheck3 = inventoryAllocator(self.items3, self.warehouse3)

        # PERSONALLY CREATED CASES (can be more, but 10 total is a good number!)

        # 4: multiple items available from 1 warehouse
        self.items4 = {'apple': 1, 'banana': 20}
        self.warehouse4 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 20} }]
        self.inventoryCheck4 = inventoryAllocator(self.items4, self.warehouse4)
        # 5: multiple items available thru a split 2 way split
        self.items5 = {'apple': 1, 'banana': 5}
        self.warehouse5 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 3}}, {'name': 'dm', 'inventory': {'banana': 5} }]
        self.inventoryCheck5 = inventoryAllocator(self.items5, self.warehouse5)
        # 6: multiple items available thru a split 3 way split
        self.items6 = {'apple': 1, 'banana': 9}
        self.warehouse6 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 3}}, {'name': 'dm', 'inventory': {'banana': 5}}, {'name': 'owo', 'inventory': {'banana':1}}]
        self.inventoryCheck6 = inventoryAllocator(self.items6, self.warehouse6)
        # 7: single item not available from list of multiple items
        self.items7 = {'apple': 1, 'banana': 5, 'mango': 2}
        self.warehouse7 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 3}}, {'name': 'dm', 'inventory': {'banana': 5, 'mango':1}}]
        self.inventoryCheck7 = inventoryAllocator(self.items7, self.warehouse7)
        # 8: multiple items not available from list of multiple items
        self.items8 = {'apple': 10, 'banana': 15}
        self.warehouse8 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 3}}, {'name': 'dm', 'inventory': {'banana': 5}}]
        self.inventoryCheck8 = inventoryAllocator(self.items8, self.warehouse8)
        # 9: empty dictionary of items
        self.items9 = {}
        self.warehouse9 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 3}}, {'name': 'dm', 'inventory': {'banana': 5}}]
        self.inventoryCheck9 = inventoryAllocator(self.items9, self.warehouse9)
        # 10: empty dictionary of warehouses
        self.items10 = {'apple': 1, 'banana': 5}
        self.warehouse10 = []
        self.inventoryCheck10 = inventoryAllocator(self.items10, self.warehouse10)

        # 11: extra fun one: if cheaper option can cover all but another warehouses down the list also has item, does algo correctly output cheaper option? 
        self.items11 = {'apple': 1, 'banana': 5, 'mango': 2}
        self.warehouse11 = [{ 'name': 'owd', 'inventory': { 'apple': 1, 'banana': 5}}, {'name': 'dm', 'inventory': {'banana': 5, 'mango':2}}]
        self.inventoryCheck11 = inventoryAllocator(self.items11, self.warehouse11)

        # run cases

        def test_main(self):
            self.assertEqual(self.inventoryCheck1.main(), [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}])
            self.assertEqual(self.inventoryCheck2.main(), [{'owd': {'apple': 1}}])
            self.assertEqual(self.inventoryCheck3.main(), [])
            self.assertEqual(self.inventoryCheck4.main(), [{'owd': {'apple': 1}}, {'owd': {'banana': 20}}])
            self.assertEqual(self.inventoryCheck5.main(), [{'owd': {'apple': 1}}, {'owd': {'banana': 3}}, {'dm': {'banana': 2}}])
            self.assertEqual(self.inventoryCheck6.main(), [{'owd': {'apple': 1}}, {'owd': {'banana': 3}}, {'dm': {'banana': 5}}, {'owo': {'banana': 1}}])
            self.assertEqual(self.inventoryCheck7.main(), [])
            self.assertEqual(self.inventoryCheck8.main(), [])
            self.assertEqual(self.inventoryCheck9.main(), [])
            self.assertEqual(self.inventoryCheck10.main(), [])
            self.assertEqual(self.inventoryCheck11.main(), [{'owd': {'apple': 1}}, {'owd': {'banana': 5}}, {'dm': {'mango': 2}}])


if __name__ == '__main__':
    unittest.main()