def candles(candlesNumber, makeNew):
    burn = 0
    leftover = 0
    n = candlesNumber
    while (n + leftover) > makeNew-1:
        burn += n
        current_parts = n + leftover
        leftover = 0 + current_parts%makeNew
        n = current_parts/makeNew
        leftover = current_parts%makeNew
        print current_parts, n, leftover, burn
    burn += n
    return burn
