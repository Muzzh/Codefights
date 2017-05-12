def isInformationConsistent(evid):
    c = [[evid[x][y] for x in range(len(evid))] for y in range(len(evid[0]))]
    print c
    for i in c:
        if -1 in i and 1 in i:
            return False
    return True
