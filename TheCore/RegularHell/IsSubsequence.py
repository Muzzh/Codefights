def isSubsequence(t, s):
    pattern = ''
    for ch in s:
        pattern += r'.*' '[' + ch + ']'
        print pattern
    return re.search(pattern, t) is not None
