def leastFactorial(n):
    for i in range(1, 6):
        temp = i
        k = 1
        while temp >= 1:
            k = k*temp
            temp -= 1
        if k >= n:
            return k
