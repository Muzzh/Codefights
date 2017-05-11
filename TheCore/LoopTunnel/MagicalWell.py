def magicalWell(a, b, n):
    tot = 0
    while n > 0 :
        tot += (a*b)
        a += 1
        b += 1
        n -= 1
    return tot
