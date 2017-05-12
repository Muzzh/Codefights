def newNumeralSystem(number):
    number = string.ascii_uppercase.index(number)
    converter = string.ascii_uppercase
    sums = set()
    for i in range(26):
        for j in range(26):
            if j + i == number:
                to_add = [j, i]
                to_add = tuple(sorted(to_add))
                sums.add(to_add)
    sums = list(sums)
    letters = []
    for i in range(len(sums)):
        letters.append((converter[sums[i][0]] + ' + ' + converter[sums[i][1]]))

    return sorted(letters)
