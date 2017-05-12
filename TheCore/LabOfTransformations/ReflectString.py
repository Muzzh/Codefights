def reflectString(inputString):
    letters = []
    rev_ascii = string.ascii_lowercase[::-1]
    ascii = string.ascii_lowercase
    for i in inputString:
        letters.append(rev_ascii[ascii.index(i)])
    return ''.join(letters)
