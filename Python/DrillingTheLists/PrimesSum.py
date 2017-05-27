def primesSum(a, b):
    return sum([x for x in range(a, b+1) if not any(y for y in xrange(2,1+int(math.sqrt(x))) if not x%y) and x != 1])
