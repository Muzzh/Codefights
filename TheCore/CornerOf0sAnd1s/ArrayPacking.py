def arrayPacking(a):
    res = 0
    i = 0
    shift = 0
    for i in range(len(a)):
        res += (a[i] << shift)
        shift += 8
        i += 1
    return res
