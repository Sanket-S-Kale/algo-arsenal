import unittest
from quick_sort import QuickSort

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.qs = QuickSort()

    def test_quicksort(self):
        arr = [10, 7, 8, 9, 1, 5]
        expected = [1, 5, 7, 8, 9, 10]
        self.qs.quickSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_quicksort_empty(self):
        arr = []
        expected = []
        self.qs.quickSort(arr, 0, len(arr) - 1) # type: ignore
        self.assertEqual(arr, expected)

    def test_quicksort_single_element(self):
        arr = [1]
        expected = [1]
        self.qs.quickSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_quicksort_duplicates(self):
        arr = [4, 2, 2, 8, 3, 3, 1]
        expected = [1, 2, 2, 3, 3, 4, 8]
        self.qs.quickSort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

if __name__ == "__main__":
    unittest.main()
