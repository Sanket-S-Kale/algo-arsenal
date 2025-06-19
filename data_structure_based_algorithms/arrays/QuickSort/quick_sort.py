# This class contains a method to sort a list of numbers using QuickSort
class QuickSort:

    # This is the main QuickSort function.
    # It sorts the part of the list from index 'low' to 'high'
    # Quick Sort uses the Divide & Conquer strategy
    def quickSort(self, arr: list[int], low: int, high: int) -> list[int]:
        # We sort only if there are at least two elements
        if low < high:
            # Find the correct position (index) of the pivot element
            pivot_index = self._partition(arr, low, high)
            
            # Recursively sort the part before the pivot
            self.quickSort(arr, low, pivot_index - 1)
            
            # Recursively sort the part after the pivot
            self.quickSort(arr, pivot_index + 1, high)
        
        # Return the sorted array
        return arr

    # This function chooses a pivot (last element at index high)
    # and arranges elements so that all smaller elements are on the left,
    # and bigger ones are on the right.
    def _partition(self, arr: list[int], low: int, high: int) -> int:
        # Choose the last element as the pivot
        pivot = arr[high]

        # Start from the left and right ends
        i, j = low, high - 1
        
        # Keep going until the pointers cross
        while i < j:
            # Move the left pointer until you find something >= pivot
            while i < high and arr[i] < pivot:
                i += 1
            
            # Move the right pointer until you find something < pivot
            while j > low and arr[j] >= pivot:
                j -= 1

            # If the left pointer is still before the right,
            # swap the two elements
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # After the loop, if the current number is bigger than pivot,
        # put the pivot in its correct place
        if arr[i] > pivot:
            arr[i], arr[high] = arr[high], arr[i]
        
        # Return the index of the pivot (where it ended up)
        return i  # Fixed: return `i` instead of `j` for correctness

# Example usage:
if __name__ == "__main__":
    qs = QuickSort()  # Create an object of the QuickSort class
    array = [4, 2, 2, 8, 3, 3, 1]  # A list of numbers to sort
    print("Original array:", array)
    qs.quickSort(array, 0, len(array) - 1)  # Sort the list using QuickSort
    print("Sorted array:", array)


# Time Complexity:
# Best case: O(n log n)
# Average case: O(n log n)
# Worst case: O(n^2)

# Space Complexity:
# Worst case: O(n) auxiliary stack space (when the recursion is unbalanced)
# Best/Average case: O(log n) auxiliary stack space (when the recursion is balanced)