# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr1, arr2):
    elements = len(arr1) + len(arr2)
    merged_arr = [0] * elements

    # Check if one of the lists is empty
    if not len(arr1) or not len(arr2):
        return arr1 or arr2  # Return the list that is not empty

    # initializing the current indices for merged_arr[i], arr1[j] and arr2[k]
    i, j, k = 0, 0, 0

    # loops while the end of both lists has not been reached
    while j < len(arr1) or k < len(arr2):
        # if the end of arr2 has not been reached and the end of arr1 has been reached or arr1[j] >= arr2[k]
        if k < len(arr2) and (j >= len(arr1) or arr1[j] >= arr2[k]):
            merged_arr[i] = arr2[k]  # The value arr2[k] is stored at i in merged_arr
            k += 1  # increment the current index of arr2
            i += 1  # increment the current index of merged_arr
        else:
            merged_arr[i] = arr1[j]  # The value arr1[j] is stored at i in merged_arr
            j += 1  # increment the current index of arr1
            i += 1  # increment the current index of merged_arr

    return merged_arr  # Return the two lists merged

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if the length is less than 2 then just return the list
    if len(arr) >= 2:
        mid = len(arr) // 2  # Calculate the middle element's index by using floor division
        # merge the sorted first half and second have of the list
        arr = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return arr

"""
STRETCH: implement the recursive logic for merge sort in a way that doesn't utilize any extra memory
In other words, your implementation should not allocate any additional lists or data structures; 
it can only re-use the memory it was given as input
"""
def merge_in_place(arr, start, mid, end):
    # Your code here
    return


def merge_sort_in_place(arr, l, r):
    # Your code here
    return

