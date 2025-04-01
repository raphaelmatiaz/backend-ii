def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Outer loop for passes
        swapped = False  # Flag to detect swaps
        for j in range(n - 1 - i):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set flag to True since a swap happened
        
        if not swapped:  # If no swaps occurred, break early
            break  

# Example usage:
arr = [3, 1, 4, 2, 5]
bubble_sort(arr)
print("Sorted array:", arr)
