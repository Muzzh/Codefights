def areIsomorphic(array1, array2):
    longuest = max(len(array1), len(array2))
    for i in range(longuest):
        try:
            if len(array1[i]) != len(array2[i]):
                return False
        except IndexError:
            return False
    return True
