def validTime(time):
    return int(time[:2]) in range(24) and int(time[3:]) in range(60) and time[2] == ':'

    
