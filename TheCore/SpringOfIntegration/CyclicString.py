def cyclicString(s):
    S = list(s)
    for i in range(1, len(s)):
        yes = 0
        a = list(s[:i])
        for j in range(len(S)):
            if S[j] in a:
                yes += 1
        if yes == len(S):
            return len(s[:i])
