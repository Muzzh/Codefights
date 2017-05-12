def sortByHeight(a):
    ppl = sorted([x for x in a if x != -1])
    track = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = ppl[track]
            track += 1
    return a
