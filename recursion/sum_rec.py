def sum_rec(n):
    if n == 0:
        return 0
    return sum_rec(n-1) + n


print(sum_rec(4))
