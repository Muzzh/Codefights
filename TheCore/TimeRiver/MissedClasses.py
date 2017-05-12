def missedClasses(year, daysOfTheWeek, holidays):
    import datetime
    redos = 0
    daysOfTheWeek = [x-1 for x in daysOfTheWeek]
    holidays = [str(x) for x in holidays]
    holi = []
    for i in range(len(holidays)):
        if int(holidays[i][:2]) > 8:
            d = datetime.date(year, int(holidays[i][:2]), int(holidays[i][3:]))
        else:
            d = datetime.date(year+1, int(holidays[i][:2]), int(holidays[i][3:]))
        holi.append(d)
    for i in holi:
        if i.weekday() in daysOfTheWeek:
            redos += 1
    return redos

    
