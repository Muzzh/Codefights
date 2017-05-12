def curiousClock(someTime, leavingTime):
    import datetime
    someTime = someTime[:10] + someTime[11:]
    leavingTime = leavingTime[:10] + leavingTime[11:]
    someTime = datetime.datetime.strptime(someTime, "%Y-%m-%d%H:%M")
    leavingTime = datetime.datetime.strptime(leavingTime, "%Y-%m-%d%H:%M")
    diff = leavingTime - someTime
    return str(someTime - diff)[:16]

    
