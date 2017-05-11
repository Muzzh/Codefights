def mostFrequentDigitSum(n):

    def step(n):
        dig_tot = sum(int(x) for x in str(n))
        n -= dig_tot
        sums.append(dig_tot)
        return n

    sums = []

    while n > 0:
        n = step(n)
    if n == 0:
        sums.append(n)
    sums = reversed(sorted(sums))
    counts = {}
    for i in sums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    from collections import defaultdict
    b = defaultdict(list)
    for key, val in counts.iteritems():
        b[val].append(key)
    return max(b[max(b)])


    
