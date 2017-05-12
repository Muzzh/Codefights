def alphabetSubsequence(s):
    for i in range(len(s)-1):
        if s.count(s[i]) > 1:
            return False
        if s[i] > s[i+1]
    return True
