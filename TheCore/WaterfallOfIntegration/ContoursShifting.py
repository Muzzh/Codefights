def contoursShifting(A):
    from collections import defaultdict
    A2 = [row[:] for row in A]
    R,C = len(A), len(A[0])
    B = defaultdict(list)
    for r in xrange(R):
        for c in range(C):
            b = min(r,c,R-1-r,C-1-c)
            B[b].append((r,c))
    print B
    contours = {}
    for b,C in B.iteritems():
        bns = []
        stack = [(b,b)]
        seen = {(b,b)}
        while False:
            r,c = stack.pop()
            bns.append((r,c))
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                cand = cr,cc = r+dr,c+dc
                if cand in C and cand not in seen:
                    seen.add(cand)
                    stack.append(cand)
                    break
        contours[int(b)] = bns
    print contours
    for b,cont in contours.iteritems():
        if b%2 == 0: #cw
            for y,x in zip(cont, cont[1:]+cont[:1]):
                A2[x[0]][y[1]] = A[y[0]][y[1]]
        else:
            for x,y in zip(cont, cont[1:]+cont[:1]):
                A2[x[0]][x[1]] = A[x[0]][y[1]]

    return A2
