import unittest
from merge_sort import MergeSort

class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.ms = MergeSort()

    def test_empty_array(self):
        arr = []
        self.ms.merge_sort(arr) # type: ignore
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [42]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [42])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])

    def test_array_with_duplicates(self):
        arr = [2, 3, 2, 1, 3, 1]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [1, 1, 2, 2, 3, 3])

    def test_array_with_negative_numbers(self):
        arr = [0, -1, 5, -10, 8, 7]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [-10, -1, 0, 5, 7, 8])

    def test_large_numbers(self):
        arr = [1000000, 999999, 123456789, -123456789]
        self.ms.merge_sort(arr)
        self.assertEqual(arr, [-123456789, 999999, 1000000, 123456789])

if __name__ == '__main__':
    unittest.main()