# MergeSort class implements the merge sort algorithm, which is a way to sort a list of numbers.
# Merge sort works by dividing the list into smaller parts, sorting those parts, and then combining them back together.

class MergeSort:
    def merge_sort(self, arr: list[int]) -> None:
        """
        Sorts the input list 'arr' in place using the merge sort algorithm.

        Args:
            arr (list[int]): The list of integers to be sorted.
        """
        length = len(arr)
        # If the list has more than one element, we need to split and sort it
        if length > 1:
            mid = length // 2  # Find the middle index to split the list
            left_arr = arr[:mid]  # Left half of the list
            right_arr = arr[mid:]  # Right half of the list

            # Recursively sort both halves
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)

            # Merge the sorted halves back into the original list
            self._merge(arr, left_arr, right_arr)
    
    def _merge(self, arr: list[int], left: list[int], right: list[int]) -> None:
        """
        Merges two sorted lists ('left' and 'right') into the original list 'arr' in sorted order.

        Args:
            arr (list[int]): The original list to store the merged result.
            left (list[int]): The left half, already sorted.
            right (list[int]): The right half, already sorted.
        """
        i, j, k = 0, 0, 0  # i: index for left, j: index for right, k: index for arr

        # Compare elements from left and right lists and copy the smaller one into arr
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]  # Copy from left if it's smaller
                i += 1
            else:
                arr[k] = right[j]  # Copy from right if it's smaller or equal
                j += 1
            k += 1
        
        # If there are remaining elements in left, copy them all
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # If there are remaining elements in right, copy them all
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Example usage
if __name__ == '__main__':
    ms = MergeSort()
    arr = [1, 5, 3, 2, 7, 6, 0, 13, 9]
    print('Original Array: ', arr)
    ms.merge_sort(arr)
    print('Sorted Array: ', arr)

# Time Complexity:
# Best case: O(n log n)
# Average case: O(n log n)
# Worst case: O(n log n)

# Space Complexity:
# Merge sort requires additional space for the temporary arrays used during merging.
# Space complexity: O(n), where n is the number of elements in the input list.