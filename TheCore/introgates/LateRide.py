def lateRide(n):
    h = str(n/60) + str(n%60)
    return sum(int(x) for x in h)
    
