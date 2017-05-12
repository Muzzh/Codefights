def allLongestStrings(inputArray):
    return [x for x in inputArray if len(x) == max(len(y) for y in inputArray)]
