def circleOfNumbers(n, firstNumber):
    d = {x:x+(n/2) for x in range(n/2)}
    d2 = {v:k for k,v in d.iteritems()}
    if firstNumber in d:
        return d[firstNumber]
    else:
        return d2[]
