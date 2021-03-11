# def calculate_itr(n):
#     while n > 0:
#         k = n ** 2
#         print(k)
#         n = n - 1


# calculate_itr(4)

# Tail recursion
# def calculate_rec(n):
#     if n > 0:
#         k = n ** 2
#         print(k)
#         calculate_rec(n-1)


# calculate_rec(4)

# Head recursion
# def calculate_rec(n):
#     if n > 0:
#         calculate_rec(n-1)
#         k = n ** 2
#         print(k)


# calculate_rec(4)

# Tree Recursion

def calculate_rec(n):
    if n > 0:
        calculate_rec(n-1)
        k = n ** 2
        print(k)
        calculate_rec(n-1)


calculate_rec(3)
