def constructSquare(s):
    r = -1
    used = {}
    for c in s:
        if c in used:
            used[c]+=1
        else:
            used[c]= 1
    h_s = used.values()
    h_s.sort()
    for i in range(int(math.sqrt(10**(len(s)-1)))+1, int(math.sqrt(10**len(s)))+1):
        p = str(i*i)
        print (p)
        if len(s)!=len(p):
            continue
        used = {}
        for c in p:
            if c in used:
                used[c]+=1
            else:
                used[c]= 1
        h_p = used.values()
        h_p.sort()
        if h_s == h_p:
            r = i*i
    return r 
