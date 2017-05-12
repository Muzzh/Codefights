def uniqueDigitProducts(a):
    for i in range(len(a)):
        a[i] = [int(x) for x in str(a[i])]
        a[i] = reduce(lambda x, y: x*y, a[i])
    return len(set(a))
