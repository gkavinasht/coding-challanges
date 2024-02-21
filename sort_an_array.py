# 912. Sort an Array
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Merge Sort
# Approach - 1
def merge(left, right):
    results = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    while i < len(left):
        results.append(left[i])
        i += 1

    while j < len(right):
        results.append(right[j])
        j += 1

    return results


def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left, right)

nums = [10, 24, 76, 73]
print(mergeSort(nums))


# Approach - 2
def mergeSortArray(nums):
    tempArr = [0] * len(nums)

    # Function to merge two sub-arrays in sorted order.
    def merge(left, mid, right):
        # Calculate the start and sizes of two halves.
        start1 = left
        start2 = mid + 1
        n1 = mid - left + 1
        n2 = right - mid

        # Copy elements of both halves into a temporary array.
        for i in range(n1):
            tempArr[start1 + i] = nums[start1 + i]
        for i in range(n2):
            tempArr[start2 + i] = nums[start2 + i]

        # Merge the sub-arrays 'in tempArr' back into the original array 'nums' in sorted order.
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if tempArr[start1 + i] <= tempArr[start2 + j]:
                nums[k] = tempArr[start1 + i]
                i += 1
            else:
                nums[k] = tempArr[start2 + j]
                j += 1
            k += 1

         # Copy remaining elements
        while i < n1:
            nums[k] = tempArr[start1 + i]
            i += 1
            k += 1
        while j < n2:
            nums[k] = tempArr[start2 + j]
            j += 1
            k += 1


    # Recursive function to sort an array using merge sort
    def merge_sort(left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        # Sort first and second halves recursively.
        merge_sort(left, mid)
        merge_sort(mid + 1, right)

        # Merge the sorted halves.
        merge(left, mid, right)

    merge_sort(0, len(nums) - 1)
    return nums

    # Time Complexity: O(nlogn)
	# Space Complexity: O(n)


# Heap Sort
def heapSortArray(nums):
    # Function to heapify a subtree (in top-down order) rooted at index i.
    def heapify(n, i):
        # Initialize largest as root 'i'.
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # If left child is larger than root.
        if left < n and nums[left] > nums[largest]:
            largest = left
        # If right child is larger than largest so far.
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If largest is not root, swap root with largest element
        # Recursively heapify the affected sub-tree (i.e. move down).
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    def heap_sort():
        n = len(nums)
        # Build heap; heapify (top-down) all elements except leaf nodes.
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        
        # Traverse elements one by one, to move current root to end, and
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            # call max heapify on the reduced heap.
            heapify(i, 0)

    heap_sort()
    return nums

    # Time Complexity: O(nlogn)
	# Space Complexity: O(logn)

# Counting Sort
def countSortArray(nums):
    def counting_sort():
        # Create the counting hash map.
        counts = {}
        # Find the minimum and maximum values in the array.
        minVal, maxVal = min(nums), max(nums)
        
        # Update element's count in the hash map.
        for val in nums:
            counts[val] = counts.get(val, 0) + 1

        index = 0
        # Place each element in its correct position in the array.
        for val in range(minVal, maxVal + 1, 1):
            # Append all 'val's together if they exist.
            while counts.get(val, 0) > 0:
                nums[index] = val
                index += 1
                counts[val] -= 1

    counting_sort()
    return nums

    # Time Complexity: O(n + k)
	# Space Complexity: O(n)

nums = [5,2,3,1]
# print(mergeSortArray(nums))
# print(heapSortArray(nums))
print(countSortArray(nums))

# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), 
# while the positions of other numbers are changed (for example, 1 and 5).