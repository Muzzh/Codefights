def isUnstablePair(filename1, filename2):
    if filename1 < filename2:
        if filename1.upper() < filename2.upper():
            return False
    if filename1 > filename2:
        if filename1.upper() > filename2.upper():
            return False
    return True
