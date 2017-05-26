def convertTabs(code, x):
    return ''.join([x*' ' if y == '\t' else y for y in code])
