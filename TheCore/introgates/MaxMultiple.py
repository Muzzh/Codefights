def maxMultiple(divisor, bound):
    N = 0
    for i in range(1,bound+1):
        if i%divisor == 0:
            N = i
    return N
