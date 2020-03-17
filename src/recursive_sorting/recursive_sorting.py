# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    sorted_arr = [0] * elements
    # TO-DO
    i_A = 0
    i_B = 0
    for i in range(elements):
        if i_B == len(arrB):
            sorted_arr[i] = arrA[i_A]
            i_A += 1
        elif i_A == len(arrA) or arrA[i_A] > arrB[i_B]:
            sorted_arr[i] = arrB[i_B]
            i_B += 1
        else:
            sorted_arr[i] = arrA[i_A]
            i_A += 1
    return sorted_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[0:mid]), merge_sort(arr[mid:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, l_start, mid, end):
    # TO-DO

    r_start = mid + 1
    # no merging needed
    if arr[mid] < arr[r_start]:
        return arr

    # if the end of either side is met then remaining
    # elements are sorted
    while l_start <= mid and r_start <= end:
        if arr[l_start] <= arr[r_start]:
            l_start += 1
        else:
            # holding r_start temporarily
            val = arr[r_start]
            ind = r_start
            # work backwards from r_start to l_start to shift all
            # elements right preserving previous sorts
            while ind > l_start:
                arr[ind] = arr[ind-1]
                ind -= 1
            arr[l_start] = val

            # moving to next item
            l_start += 1
            # shifting end of list because "insertion" made it longer
            mid += 1
            # shifting start of list because r_start was set to mid
            r_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if not l < r:
        return arr
    else:
        m = (l + r) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)
        return merge_in_place(arr, l, m, r)


# STRETCH: implement the Timsort function below
# hint: https://github.com/python/cpython/blob/master/Objects/listsort.txt
def asc_timsert(arr, left, right):
    for i in range(left + 2, right + 1):

        low = left
        high = i-1
        pos = None

        if arr[i] > arr[high]:
            pos = i
        elif arr[i] < arr[low]:
            pos = low

        while pos is None:

            mid = (low+high) // 2

            if arr[i] == arr[mid]:
                pos = mid

            elif low == mid or high == mid:
                if arr[i] < arr[low]:
                    pos = low

                else:
                    pos = high

            elif arr[i] > arr[mid]:
                low = mid

            else:
                high = mid

        temp = arr[i]

        for el in range(i, pos-1, -1):
            arr[el] = arr[el-1]

        arr[pos] = temp
    return arr


def dsc_timsert(arr, left, right):
    print(arr)
    for i in range(left + 2, right + 1):

        low = left
        high = i-1
        pos = None
        print(arr[low:i])
        if arr[i] < arr[high]:
            pos = i
        elif arr[i] > arr[low]:
            pos = low

        while pos is None:

            mid = (low+high) // 2

            if arr[i] == arr[mid]:
                pos = mid

            elif low == mid or high == mid:
                if arr[i] < arr[low]:
                    pos = high

                else:
                    pos = low

            elif arr[i] < arr[mid]:
                low = mid

            else:
                high = mid

        temp = arr[i]

        for el in range(i, pos-1, -1):
            arr[el] = arr[el-1]

        arr[pos] = temp
    return arr


def timerge(arr, l, m, r):
    pass


def timsort(arr):
    # pull len from method
    LEN = len(arr)
    # set upper and lower bounds for a run
    RUNS = (8, 32)
    # if two runs can't be made
    if LEN < 2:
        return arr
    # if LEN < RUNS[0] * 2:
    if arr[0] <= arr[1]:
        arr = asc_timsert(arr, 0, LEN-1)
    else:
        arr = dsc_timsert(arr, 0, LEN-1)
        arr.reverse()
    # else:
    #     runs = []
    #     asc = True
    #     c_run = [-1, -1]
    #     for i in range(LEN):
    #         if c_run[1] < i:
    #             c_run[0] = i
    #             if i + RUNS[0] == LEN:
    #                 if i+1 != LEN:
    #                 i = LEN - 1
    #                 c_run[1] = i
    #                 and arr[i] > arr[i+1]
    #                 asc = False
    #                 else:
    #                     asc = True

    #         else:
    # runs = []
    # for x in range(LEN//RUN):
    # if (x+1)*RUN > LEN:
    # pass
    # else:
    # pass
    # make runs and sort them
    # merge the runs
    return arr
