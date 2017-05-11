def isMAC48Address(inputString):
    v = ('ABCDEF1234567890')
    couples = inputString.split('-')
    if len(couples) != 6:
        return False
    if len(inputString) != 17:
        return False
    for i in couples:
        if len(i) != 2:
            return False
        for j in i:
            if j in v:
                pass
            else:
                return False
    return True
