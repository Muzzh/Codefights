def newYearCelebrations(takeOffTime, minutes):
    midnight = 24*60*2
    celeb = 0
    takeOffTime = 1440 + int(takeOffTime[:2])*60 + int(takeOffTime[3:])
    if takeOffTime == 1440:
        takeOffTime = 1440 * 2
    print takeOffTime
    if len(minutes) == 0:
        if takeOffTime <= midnight:
            return 1
        return 0
    t = [minutes[0]]
    for i in range(1,len(minutes)):
        diff = minutes[i] - minutes[i-1]
        t.append(diff)
    minutes = t

    for i in range(minutes[0]):
        if takeOffTime == midnight:
            celeb += 1
        takeOffTime += 1
    if takeOffTime == midnight:
        celeb += 1
    for i in range(1,len(minutes)):
        if takeOffTime == midnight:
            celeb += 1
        takeOffTime -= 60
        for j in range(minutes[i]):
            if takeOffTime == midnight:
                celeb += 1
            takeOffTime += 1


    if takeOffTime <= midnight:
        celeb += 1
    return celeb
    
