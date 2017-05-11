def increaseNumberRoundness(n):
    N = [int(x) for x in str(n)]
    swappable = False
    for i in range(len(N)-1, -1, -1):
        if N[i] != 0:
            swappable = True
        if N[i] == 0 and swappable == True:
            return True

    return False
