def holiday(x, weekDay, month, yearNumber):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    m = months.index(month) +1
    d = week.index(weekDay)
    import calendar
    mon = calendar.monthcalendar(yearNumber,m)
    print mon
    first_day = 0
    for i in range(len(mon)):
        if mon[i][d] != 0:
            first_day = i
            break
    try:
        if mon[x-1+first_day][d] == 0:
            return -1
        else:
            return mon[x-1+first_day][d]
    except IndexError:
        return -1
