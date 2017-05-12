def areSimilar(A, B):
    if A == B:
        return True
    if sorted(A) != sorted(B):
        return False
    swaps = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            swaps += 1
    if swaps == 2:
        return True
    return False
    
