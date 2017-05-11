def isSumOfConsecutive2(n):
    poss = 0

    for i in range(n-1, -1, -1):
        tot = i
        index = 1
        while -1 < tot < n:
            to_add = i - index
            tot += to_add
            index += 1
        if tot == n:
            poss += 1
    return poss
