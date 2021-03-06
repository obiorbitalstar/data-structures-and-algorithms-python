import math


def merge_sort(arr):
    if len(arr) == 0:
        return f'This list is empty'

    n = len(arr)

    if n > 1:
        mid = math.floor(n/2)
        left = arr[0:mid]
        right = arr[mid:n]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)
    return arr


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        arr[k] = right[j]
    else:
        arr[k] = left[i]


x = [8, 4, 23, 42, 16, 15]

print(merge_sort(x))
