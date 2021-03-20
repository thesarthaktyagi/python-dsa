def power(n):
    if n < 1:
        return 'Wrong Input'
    else:
        str_n = str(n)
        len_n = len(str_n)
        power_n = n ** 4
        str_power = str(power_n)
        check = int(str_power[-len_n:])
        if n == check:
            return True
        else:
            return False


print(power(-1))
