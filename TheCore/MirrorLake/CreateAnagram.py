def createAnagram(s, t):
    op = len(t)
    s = [x for x in s]
    t = [x for x in t]

    for i in range(len(s)):
        if s[i] in t:
            del t[t.index(s[i])]
    print s, t
    return len(t)
