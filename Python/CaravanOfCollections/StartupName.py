def startupName(companies):
    comp1 = set(companies[0])
    comp2 = set(companies[1])
    comp3 = set(companies[2])
    res = [k for k,v in {x:list((list(comp1) + list(comp2) + list(comp3))).count(x) for x in set(list(comp1)+list(comp2)+list(comp3))}.items() if v ==2]
    return sorted(list(res))
