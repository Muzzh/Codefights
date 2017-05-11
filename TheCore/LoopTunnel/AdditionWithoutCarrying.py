def additionWithoutCarrying(param1, param2):
    p1 = [int(x) for x in list(str(param1))]
    p2 = [int(x) for x in list(str(param2))]
    front_add = max(len(p1),len(p2)) - min(len(p1), len(p2))
    longuest = p1
    if len(p2) > len(p1):
        longuest = p2

    tot = []
    for i in range(0,front_add):
        tot.append(longuest[i])
    del longuest[:front_add]
    for i in range(len(p1)):
        tot.append((p1[i] + p2[i])%10)

    total = [str(x) for x in tot]
    return int(''.join(total))
