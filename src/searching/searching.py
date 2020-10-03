# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = start + (end - start) // 2  # Find the current list's middle index

    # if the end value is less than the start value, entire list has been searched
    if end < start:
        return -1  # target value not in the list
    else:
        # Base case, if the current middle element is equal to target then return its index
        if arr[mid] == target:
            return mid
        # Search to the left of the middle element if target is less than the middle element
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid-1)
        # Search to the right of the middle element if target is greater than the middle element
        else:
            return binary_search(arr, target, mid+1, end)

"""
STRETCH: implement an order-agnostic binary search
This version of binary search should correctly find the target regardless of whether the input array is
sorted in ascending order or in descending order. You can implement this function either recursively or iteratively
"""
def agnostic_binary_search(arr, target):
    # set initial start and end points
    start, end = 0, len(arr) - 1

    while start <= end:
        # Calculate the current middle index for each iteration
        mid = start + (end - start) // 2

        # if the target value is found in the list return the index
        if target == arr[mid]:
            return mid
        elif arr[start] < arr[end]:  # if the list is in ascending order
            if target < arr[mid]:  # if target less than middle value then check if target is in the first half
                end = mid - 1
            else:  # if target greater than middle value then check if target is in the second half
                start = mid + 1
        else:  # if the list is in descending order
            if target > arr[mid]:  # if target greater than middle value then check if target is in the first half
                end = mid - 1
            else:  # if target less than middle value then check if target is in the second half
                start = mid + 1

    return -1  # if target not found
