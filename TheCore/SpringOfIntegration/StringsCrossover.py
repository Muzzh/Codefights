def stringsCrossover(inputArray, result):

    for i in range(len(result)):
        is_in = False
        for j in range(len(inputArray)):
            if inputArray[j][i] == result[i]:
                is_in = True
        if is_in == False:
            return 0
    couples = []
    for i in range(len(inputArray)-1):
        for j in range(i+1, len(inputArray)):
            couples.append([inputArray[i], inputArray[j]])

    poss = 0
    for i in range(len(couples)):
        matches = 0
        for j in range(len(result)):
            letters = [couples[i][x][j] for x in range(len(couples[i]))]
            if result[j] in letters:
                matches += 1
        if matches == len(result):
            poss += 1
    return poss
