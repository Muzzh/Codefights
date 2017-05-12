def higherVersion(ver1, ver2):
    ver1 = ver1.split('.')
    ver2 = ver2.split('.')
    for i in range(len(ver1)-1,-1,-1):
        ver1[i] = int(ver1[i]) * 10**abs(i-(1000*(len(ver1)-1)))
        ver2[i] = int(ver2[i]) * 10**abs(i-(1000*(len(ver1)-1)))
    print ver1, ver2
    ver1 = sum(ver1)
    ver2 = sum(ver2)

    return ver1 > ver2
