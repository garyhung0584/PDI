# n = 4
# for i in range(9):
#     print(f'({(i//3)-1+n},{(i%3)-1+n})', end=" ")
#     print()


def QuickSort(arr, start, end):
    if start < end:
        pivotIndex = partition(arr, start, end)
        QuickSort(arr, start, pivotIndex - 1)
        QuickSort(arr, pivotIndex + 1, end)
    return arr


def partition(arr, start, end):
    n = len(arr)
    pivot = arr[end]
    nextIndex = start
    for i in range(start, n - 1):
        if arr[i] < pivot:
            arr[nextIndex], arr[i] = arr[i], arr[nextIndex]
            nextIndex += 1
    arr[nextIndex], arr[end] = arr[end], arr[nextIndex]
    return nextIndex


data = [69, 81, 30, 38, 9, 2, 47, 61, 32, 79]

print(QuickSort(data, 0, len(data) - 1))  # [10, 20, 30, 40, 50, 60, 70, 80, 90]
