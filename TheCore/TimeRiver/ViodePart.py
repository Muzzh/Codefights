def videoPart(part, total):
    part = int(part[:2]) * (60 * 60) + int(part[3:5]) * 60 + int(part[6:])
    total = int(total[:2]) * (60 * 60) + int(total[3:5]) * 60 + int(total[6:])
    from fractions import gcd
    factor = gcd(part, total)
    return [part/factor, total/factor]
    
