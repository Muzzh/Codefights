def stringsConstruction(A, B):
    constructs = []
    A = list(A)
    B = list(B)
    while set(B).issuperset(set(A)) == True:
        for i in A:
            if i in B:
                index = B.index(i)
                to_add = B.pop(index)
                constructs.append(to_add)
    return len(constructs)/len(A)
