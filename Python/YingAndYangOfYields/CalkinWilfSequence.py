def calkinWilfSequence(number):
    def fractions():
        r = [0,1]
        while True:
            r = (r[1], (r[1] * (r[0] // r[1])) + (r[1] - (r[0] % r[1])))
            yield list(r)
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
