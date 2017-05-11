def isInfiniteProcess(a, b):
    if a > b:
        return True
    if a%2 != b%2:
        return True

    return False
