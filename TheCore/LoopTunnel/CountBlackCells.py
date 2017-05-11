def countBlackCells(n, m):
    from fractions import gcd
    g = gcd(n,m)
    n /= g
    m /= g

    return (n + m - 1) * g + 2*(g-1)
