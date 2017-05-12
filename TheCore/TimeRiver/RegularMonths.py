def regularMonths(currMonth):
    import datetime
    y = int(currMonth[3:])
    m = int(currMonth[:2]) +1
    left = 12-m
    print left
    for j in range(left+1):
        print j, m, m+j, 'first'
        d = datetime.date(y, m+j, 1)
        if d.weekday() == 0:
            return d.strftime('%m-%Y')

    for i in range(1,200):
        for j in range(1,13):
            print y+i, j
            d = datetime.date(y+i, j, 1)
            if d.weekday() == 0:
                return d.strftime('%m-%Y')
