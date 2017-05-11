def lineUp(commands):
    s = 0
    t = 0
#    f = ^^^^
    for i in commands:
        if i == 'L' or i == 'R':
            t += 1
        if t % 2 == 0:
            s += 1
    return s
