def arrayPreviousLess(items):
    new = [-1]
    for i in range(1, len(items)):
        there_is = False
        for j in range(len(items[:i]) -1, -1, -1):
            if items[j] < items[i]:
                new.append(items[j])
                there_is = True
                break
        if there_is == False:
            new.append(-1)
    return new
