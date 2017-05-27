def calcBonuses(bonuses, n):
    it = iter([bonuses[i] for i in range(0,n) if len(bonuses) >= n])
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
