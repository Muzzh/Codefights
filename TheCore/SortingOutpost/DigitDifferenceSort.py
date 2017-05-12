def digitDifferenceSort(a):
    b = []
    a = a[::-1]
    for i in range(len(a)):
        x = a[i]
        digits = [int(v) for v in str(a[i])]
        y = max(digits) - min(digits)
        b.append([x, y])
    b = sorted(b, key = lambda x: int(x[1]))
    return [b[x][0] for x in range(len(b))]
