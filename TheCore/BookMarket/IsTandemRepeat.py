def isTandemRepeat(inputString):
    if len(inputString)%2 == 0:
        if inputString[0:len(inputString)/2] == inputString[len(inputString)/2:]:
            return True
    return False
