def switchLights(a):
    for i in range(len(a)):
        if a[i] == 1:
            for j in range(0, i+1):
                a[j] = 1 - a[j]
    return a
