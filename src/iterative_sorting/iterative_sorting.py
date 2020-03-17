# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for n in range(i, len(arr)):
            if arr[smallest_index] > arr[n]:
                smallest_index = n
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                isSorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    # arrays of length 1 are already sorted
    if len(arr) < 2:
        return arr
    # if a max value is not given find the max value
    if maximum < 1:
        for n in arr:
            if n > maximum:
                maximum = n

    # list from 0 to maximum value used to count occurances of values
    count = [0 for i in range(0, maximum+1)]
    # the sorted array
    out = [0 for i in range(0, len(arr))]
    # count the values
    for num in arr:
        # return out if a bad value is in the array
        if num < 0 or not isinstance(num, int):
            return 'Error, negative numbers not allowed in Count Sort'
        count[num] += 1
    # make the counts equal to their value plus the sum of previous values
    for i in range(0, len(count)-1):
        count[i+1] += count[i]
    # loop from last element to first element
    for i in range(len(arr)-1, -1, -1):
        # each loop addresses arr[i]
        # count[x] is the location to place x
        # thus out[count[x]-1] should equal x
        out[count[arr[i]]-1] = arr[i]
        # after an element is placed the next equal value should be to the left
        count[arr[i]] -= 1

    return out
