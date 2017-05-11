def appleBoxes(k):
    red = 0
    yellow = 0
    for i in range(1, k+1):
        if i%2 == 0:
            red += i**2
        else:
            yellow += i**2
    return red - yellow
