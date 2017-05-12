def threeSplit(a):
    sets = 0
    if sum(a)%3 != 0:
        return 0
    mid = sum(a)/3
    for i in range(len(a)):
        if sum(a[:i]) == mid and len(a[:i]) != 0:
            if sum(a[i:]) != 2*mid:
                break
            for j in range(i+1, len(a)):
                if sum(a[i:j]) == mid:
                    sets += 1

    return sets
