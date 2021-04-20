# Write a function to return minimum and maximum in an array. Your program should make the minimum number of comparisons.

# First Approach ------------------------------------------->

# def find_min(arr):
#     minimum = arr[0]
#     for i in range(1, len(arr)):
#         if minimum > arr[i]:
#             minimum = arr[i]
#         else:
#             pass
#     return minimum


# def find_max(arr):
#     maximum = arr[0]
#     for i in range(1, len(arr)):
#         if maximum < arr[i]:
#             maximum = arr[i]
#         else:
#             pass
#     return maximum


# def min_and_max(arr):
#     print("Minimum element is : ", find_min(arr))
#     print("Maximum element is : ", find_max(arr))


# min_and_max([])

# ----------------------------------------------------------->

# Second Approach *******************************************>

class Pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> Pair:
    minmax = Pair()

    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax
    if arr[0] > arr[1]:
        minmax.min = arr[1]
        minmax.max = arr[0]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax


if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
