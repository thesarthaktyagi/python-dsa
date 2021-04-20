def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end-1
    return arr


print(reverse_array([5, 7, 3, 8, 5, 9, 2, 7, 5, 6, 3]))
print(reverse_array([5, 4, 3, 2, 1]))
