def arithmeticExpression(A, B, C):
    if A + B == C:
        print 'add'
        return True
    if A - B == C:
        print 'sub'
        return True
    if A * B == C:
        print 'mult'
        return True
    if float(A)/float(B) == C:

        return True
    return False
