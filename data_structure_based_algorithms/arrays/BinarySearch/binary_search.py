class BinarySearch:
    def binary_search(self, haystack: list[int], needle: int) -> int:
        """
        Performs binary search to find the index of a target value (needle) in a SORTED list (haystack).
        Returns:
            int: The index of the needle in the haystack if found; otherwise, -1.
        The binary search algorithm works by repeatedly dividing the search interval in half:
        - It starts by comparing the target value to the middle element of the list.
        - If the target value matches the middle element, its index is returned.
        - If the target value is less than the middle element, the search continues on the left half.
        - If the target value is greater, the search continues on the right half.
        - This process repeats until the value is found or the search interval is empty.
        Example:
            >>> binary_search([1, 3, 5, 7, 9], 5)
            2
            >>> binary_search([1, 3, 5, 7, 9], 4)
            -1
        """
        # Set the initial search boundaries: left is the first index, right is the last index
        left, right = 0, len(haystack) - 1
        # Calculate the middle index between left and right
        mid = (left + right) // 2

        # Continue searching as long as the left boundary does not cross the right
        while left <= right:
            # If the middle element is the target, return its index
            if haystack[mid] == needle:
                return mid
            # If the target is smaller than the middle element, search the left half
            elif needle < haystack[mid]:
                right = mid - 1
            else: # If the target is larger, search the right half
                left = mid + 1
            
            # Update the middle index for the next iteration
            mid = (left + right) // 2
        
        # If the target is not found, return -1
        return -1

# Example usage:
if __name__ == '__main__':
    bs = BinarySearch()
    arr = [1, 5, 7, 9, 11]
    print(bs.binary_search(arr, 91))

# Time Complexity:
# Best Case: O(1)      # The needle is found at the first middle check.
# Average Case: O(log n) # The search space is halved each time.
# Worst Case: O(log n)   # The needle is not present or is at the end of the search.

# Space Complexity:
# O(1) # Only a few variables are used, regardless of the size of the input list.