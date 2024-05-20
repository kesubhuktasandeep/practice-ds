def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    arr = []
    print("Enter the elements of the array:")
    for _ in range(size):
        arr.append(int(input()))

    selection_sort(arr)

    print("Sorted array:")
    for num in arr:
        print(num, end=" ")
