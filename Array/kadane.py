def maxSubArraySum(a, size):

    current_best = -99999999999 - 1
    overall_best = 0

    for i in range(0, size):
        overall_best = overall_best + a[i]
        if (current_best < overall_best):
            current_best = overall_best

        if overall_best < 0:
            overall_best = 0
    return current_best


# Driver function to check the above function
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))
