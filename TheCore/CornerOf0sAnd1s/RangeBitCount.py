def rangeBitCount(a, b):
    l = range(a, b+1)
    l = ["{0:b}".format(x) for x in l]

    count = 0
    for i in l:
        for j in i:
            if j == '1':
                count += 1
    return count
    
