def houseNumbersSum(inputArray):
    total = 0
    for i in inputArray:
        if i == 0:
            break
        total += i
    return total
