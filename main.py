def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
print("Sorted array:", arr)
print("Array is sorted successfully")