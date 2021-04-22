# Given an array arr[] denoting heights of N towers and a positive integer K,
#  you have to modify the height of each tower either by increasing or decreasing them by K only once.
# After modifying, height should be a non-negative integer.
# Find out what could be the possible minimum difference of the
# height of shortest and longest towers after you have modified each tower.

# Example 1:

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as
# {3, 3, 6, 8}. The difference between
# the largest and the smallest is 8-3 = 5.
# Example 2:

# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output:
# 11
# Explanation:
# The array can be modified as
# {6, 12, 9, 13, 17}. The difference between
# the largest and the smallest is 17-6 = 11.


class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def minHeight(arr, k):
    minMax = Pair()
    minMax.min = 999999999999
    minMax.max = 999999999999
    height_mean = sum(arr)/len(arr)
    for i in range(0, len(arr)):
        if arr[i] < height_mean:
            arr[i] = k + arr[i]
            if arr[i] < minMax.min:
                minMax.min = arr[i]
            else:
                minMax.max = arr[i]
        elif arr[i] >= height_mean:
            arr[i] = arr[i] - k
            if arr[i] < minMax.min:
                minMax.min = arr[i]
            else:
                minMax.max = arr[i]
    return minMax.max - minMax.min


print(minHeight([3, 9, 12, 16, 20], 3))
