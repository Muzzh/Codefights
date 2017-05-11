def weakNumbers(n):

    def d(n):
        num = 0
        for i in range(1, n+1):
            if n%i == 0:
                num += 1
        return num

    def weakness(n):
        weakness = 0
        for i in range(n):
            if dividers[i][1] > dividers[n][1]:
                weakness += 1
        return weakness

    dividers = []
    for i in range(0, n+1):
        dividers.append([i, d(i)])

    weaknesses = []
    for i in range(len(dividers)):
        weaknesses.append([i, weakness(i)])

    max_weak = max([weaknesses[x][1] for x in range(len(weaknesses))])
    occurence = 0
    for i in range(1,len(weaknesses)):
        print i, weaknesses[i], max_weak
        if weaknesses[i][1] == max_weak:
            occurence += 1
    return [max_weak, occurence]
