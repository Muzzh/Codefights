def coolPairs(a, b):
    uniqueSums = {k:+1 for k in set([x+y for y in a for x in b if (x*y)%(x+y)==0])}
    return len(uniqueSums)
