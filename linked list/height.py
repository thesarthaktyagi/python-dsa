def height(size, arr):
    result = [1]*size
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            print("first")
            continue
        else:
            tmp = arr[:i+1]
            for j in range(len(tmp)-1, -1, -1):
                if tmp[j] < tmp[len(tmp)-1]:
                    count += 1
                result[i] = result[i] + count
                count = 0
    return result


print(height(4, [2, 5, 1, 7]))


# [2, 5, 1, 7, 9, 1 ,3]  ===>> [1, 1, 1, 3, 4, 1, 2]
