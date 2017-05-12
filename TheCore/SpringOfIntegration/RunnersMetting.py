def runnersMeetings(startPosition, speed):
    from collections import Counter
    couples = []
    for i in range(len(startPosition)):
        couples.append([startPosition[i], float(speed[i])/60])

    if len(startPosition) < 2:
        return -1
    if len(startPosition) == 2:
        if startPosition[0] < startPosition[1] and speed[0] > speed[1]:
            return 2
        elif startPosition[0] > startPosition[1] and speed[0] < speed[0]:
            return 2
        else:
            return -1

    cardinalities = []
    top = max(startPosition)
    for i in range(top**2, top**2 + top*100) :
        print i
        distances = []
        for j in range(len(couples)):
            d = i * couples[j][1] + couples[j][0]
            distances.append(d)

        if Counter(distances).most_common(1)[0][1] > 1:
            cardinalities.append(Counter(distances).most_common(1)[0][1])
    if len(cardinalities) == 0:
        return -1
    return max(cardinalities)
