def combs(comb1, comb2):
    c1 = []
    c2 = []
    for i in range(len(comb1)):
        if comb1[i] == '*':
            c1.append(1)
        else:
            c1.append(0)
    for i in range(len(comb2)):
        if comb2[i] == '*':
            c2.append(1)
        else:
            c2.append(0)

    max_lenght = len(c1) + len(c2)
    int_c1 = int(''.join([str(x) for x in c1]),2)
    int_c2 = int(''.join([str(x) for x in c2]),2)

    poss = []
    for i in range(len(c2), 0, -1):
        a = int_c1<<i
        if int_c2&a == 0:
            poss.append(i+len(c1))

    for i in range(len(c1)+len(c2)):
        a = int_c2<<i
        leng_a = len("{0:b}".format(a))
        if int_c1&a == 0:
            if i <= len(c1) - len(c2):
                poss.append(len(c1))
            else:
                poss.append(leng_a)

    return min(poss)
