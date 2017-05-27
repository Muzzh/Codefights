def calcFinalScore(scores, n):
    gen = reversed(sorted(scores[x]*scores[x] for x in range(len(scores))))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res /= 5

    return res
