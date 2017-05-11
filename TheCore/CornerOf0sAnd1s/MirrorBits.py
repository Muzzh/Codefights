def mirrorBits(a):
    A = list(str("{0:b}".format(a)))
    A = A[::-1]
    return int(''.join(A),2)
