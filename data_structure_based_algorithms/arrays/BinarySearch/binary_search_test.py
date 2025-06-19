import unittest
from binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()

    def test_found_in_middle(self):
        arr = [1, 5, 7, 9, 11]
        self.assertEqual(self.bs.binary_search(arr, 7), 2)

    def test_found_at_start(self):
        arr = [1, 5, 7, 9, 11]
        self.assertEqual(self.bs.binary_search(arr, 1), 0)

    def test_found_at_end(self):
        arr = [1, 5, 7, 9, 11]
        self.assertEqual(self.bs.binary_search(arr, 11), 4)

    def test_not_found(self):
        arr = [1, 5, 7, 9, 11]
        self.assertEqual(self.bs.binary_search(arr, 91), -1)

    def test_empty_list(self):
        arr = []
        self.assertEqual(self.bs.binary_search(arr, 5), -1) # type: ignore

    def test_single_element_found(self):
        arr = [5]
        self.assertEqual(self.bs.binary_search(arr, 5), 0)

    def test_single_element_not_found(self):
        arr = [5]
        self.assertEqual(self.bs.binary_search(arr, 1), -1)

    def test_even_number_of_elements(self):
        arr = [2, 4, 6, 8]
        self.assertEqual(self.bs.binary_search(arr, 6), 2)
        self.assertEqual(self.bs.binary_search(arr, 2), 0)
        self.assertEqual(self.bs.binary_search(arr, 8), 3)
        self.assertEqual(self.bs.binary_search(arr, 5), -1)

    def test_negative_numbers(self):
        arr = [-10, -5, 0, 5, 10]
        self.assertEqual(self.bs.binary_search(arr, -5), 1)
        self.assertEqual(self.bs.binary_search(arr, 0), 2)
        self.assertEqual(self.bs.binary_search(arr, 10), 4)
        self.assertEqual(self.bs.binary_search(arr, -11), -1)

if __name__ == '__main__':
    unittest.main()