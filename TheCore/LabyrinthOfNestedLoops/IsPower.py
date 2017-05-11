def isPower(n):
    for a in range(1,21):
        for b in range(2,11):
            print a**b
            if a ** b == n:
                return True
    return False
