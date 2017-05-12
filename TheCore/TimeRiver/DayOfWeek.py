def dayOfWeek(birthdayDate):
    import datetime
    year = int(birthdayDate[6:])
    month = int(birthdayDate[:2])
    day = int(birthdayDate[3:5])
    D_day = datetime.date(year,month,day).weekday()
    for i in range(1,100):
        try:
            if datetime.date(year+i, month, day).weekday() == D_day:
                return year+i - year
        except ValueError:
            pass
    
