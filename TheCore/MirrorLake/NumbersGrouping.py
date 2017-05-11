def numbersGrouping(a):
    groups = {}
    for i in a:
        t = i -1
        v = (t) - (t%10**4)
#        print v, i
        v = "{:.4e}".format(v)
        if v not in groups:
            groups[v] = 1
        else:
            groups[v] += 1
    lines = 0
    for key in groups:
        lines += groups[key]

    return lines + len(groups)



        
