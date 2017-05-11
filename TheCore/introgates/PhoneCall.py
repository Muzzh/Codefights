def phoneCall(min1, min2_10, min11, s):
    tot = 0
    if s > min1:
        s -= min1
        tot += 1
        print tot, s
    step = 2
    while step < 11 and s >= min2_10:
        s -= min2_10
        tot += 1
        step += 1
        print tot, s, '2-10'
    if step == 11:
        while s >= min11:
            s -= min11
            tot += 1
        print tot, s
    return tot
