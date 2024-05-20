def merge(arr, left, mid, right):
    sizeFirst = mid - left + 1
    sizeSecond = right - mid

    firstArr = arr[left:left + sizeFirst]
    secondArr = arr[mid + 1:mid + 1 + sizeSecond]

    i = j = 0
    k = left

    while i < sizeFirst and j < sizeSecond:
        if firstArr[i] < secondArr[j]:
            arr[k] = firstArr[i]
            i += 1
        else:
            arr[k] = secondArr[j]
            j += 1
        k += 1

    while i < sizeFirst:
        arr[k] = firstArr[i]
        i += 1
        k += 1

    while j < sizeSecond:
        arr[k] = secondArr[j]
        j += 1
        k += 1

def mergeSortUtil(arr, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2

    mergeSortUtil(arr, left, mid)
    mergeSortUtil(arr, mid + 1, right)

    merge(arr, left, mid, right)

def mergeSort(arr):
    mergeSortUtil(arr, 0, len(arr) - 1)
