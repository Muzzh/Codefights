def metroCard(lastNumberOfDays):
    days = [31,28,31,30,31,30,31,31,30,31,30,31,31]
    index = []
    for i, v in enumerate(days):
        if v == lastNumberOfDays and i < 12:
            index.append(i)
    new = [days[x+1] for x in index]
    answer = []
    for i in new:
        if i not in answer:
            answer.append(i)
    return answer
