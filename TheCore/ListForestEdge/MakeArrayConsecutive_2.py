def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    adds = 0
    for i in range(statues[0], statues[len(statues)-1]):
        if i not in statues:
            adds += 1
    return adds
