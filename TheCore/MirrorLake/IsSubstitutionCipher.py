def isSubstitutionCipher(s1, s2):
    if len(s1) != len(s2):
        return False

    couples = []
    for i in range(len(s1)):
        couples.append([s1[i], s2[i]])

    letters = {}
    for i in range(len(couples)):
        if couples[i][0] not in letters:
            letters[couples[i][0]] = couples[i][1]
        elif letters[couples[i][0]] != couples[i][1]:
            return False
        else:
            pass

    rev_letters = {}
    for i in range(len(couples)):
        if couples[i][1] not in rev_letters:
            rev_letters[couples[i][1]] = couples[i][0]
        elif rev_letters[couples[i][1]] != couples[i][0]:
            return False
        else:
            pass
    return True
