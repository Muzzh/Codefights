def pairOfShoes(shoes):
    new = []
    for i in shoes:
        new.append(i[1])
    print new.count(23)
    pairs = sum([shoes[x][0] for x in range(len(shoes))])
    if pairs != len(shoes)/2:
        return False
    size_0 = {str(shoes[i][1]): +1 for i in range(len(shoes)) if shoes[i][0] == 0}
    size_1 = {str(shoes[i][1]): +1 for i in range(len(shoes)) if shoes[i][0] == 1}
    print size_0, size_1
    for k in size_0:
        while size_0[k]  != 0:
            if k in size_1:
                size_0[k] -= 1
                size_1[k] -= 1
            else:
                break
    for k in size_0:
        if size_0[k] != 0:
            return False
    for k in size_1:
        if size_1[k] != 0:
            return False
    return True
