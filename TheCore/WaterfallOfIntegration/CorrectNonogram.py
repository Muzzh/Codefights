def correctNonogram(size, nono):
    size = (size+1) / 2 + size
    if len(nono) != size: return 0
    for i in nono:
        if len(i) != size: return 0

    columns = [[nono[x][y] for x in range(len(nono))] for y in range(len(nono[0]))]

    lines = []
    for i in nono:
        if '#' in i:
            lines.append(i)
    for i in columns:
        if '#' in i:
            lines.append(i)

    for i in lines:
        nums = []
        for j in i:
            if str(j).isdigit() == True:
                nums.append(int(j))
        sequences = []
        j = 0
        while j < len(i):
            if i[j] == '#':
                to_add = 1
                try:
                    while i[j+to_add] == '#':
                        to_add += 1
                except IndexError:
                    pass
                j += to_add
                sequences.append(to_add)
            else:
                j += 1
        if nums == sequences:
            pass
        else:
            print i, nums, sequences
            return 0
    return 1
