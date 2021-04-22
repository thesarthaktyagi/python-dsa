# Given an array of integers where each element represents the max number of steps
# that can be made forward from that element. Find the minimum number of jumps to reach
# the end of the array (starting from the first element). If an element is 0, then you cannot
# move through that element.

# Example 1:

# Input:
# N=11
# arr=1 3 5 8 9 2 6 7 6 8 9
# Output: 3
# Explanation:
# First jump from 1st element to 2nd
# element with value 3. Now, from here
# we jump to 5th element with value 9,
# and from here we will jump to last.
# Example 2:

# Input :
# N= 6
# arr= 1 4 3 2 6 7
# Output: 2
# Explanation:
# First we jump from the 1st to 2nd element
# and then jump to the last element.


# def minJump(arr):
#     n = len(arr)
#     element = 0
#     count = 0
#     while element < n:
#         if arr[element] == arr[n-1]:
#             print("arr[element] : ", arr[element])
#             break
#         else:
#             element += arr[element]
#             print("element : ", element)
#             count += 1
#         print("Count : ", count)
#     return count

def minJump(arr):
    if len(arr) == 1:
        return 0
    n = len(arr)
    curr_reach = 0
    max_reach = 0
    jumps = 0

    for i in range(0, n):
        if i + arr[i] >= n - 1:
            return jumps + 1
        elif i + arr[i] > max_reach:
            max_reach = i + arr[i]
        elif i == curr_reach:
            jumps += 1
            curr_reach = max_reach
    return jumps


print(minJump([1, 4, 3, 2, 6, 7]))
print(minJump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
