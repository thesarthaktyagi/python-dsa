# Given two arrays a[] and b[] of size n and n respectively. The task is to find union between these two arrays.
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
#  If there are repetitions, then only one occurrence of element should be printed in union.

# Example:

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3

# Output:
# 5

# Explanation:
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.


def arrUnion(arr1, arr2):
    union = set(arr1 + arr2)
    l = len(union)
    return l


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(arrUnion(arr1, arr2))
