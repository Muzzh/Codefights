def willYou(young, beautiful, loved):
    if young == True and beautiful == True and loved== False:
        return True
    if young == False and beautiful == False and loved == True:
        return True
    if young == True and beautiful == False and loved == True:
        return True
    if young == False and beautiful == True and loved == True:
        return True
    return False
