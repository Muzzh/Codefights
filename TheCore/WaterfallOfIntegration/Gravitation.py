def gravitation(R):
    columns = [[R[r][c] for r in range(len(R))] for c in range(len(R[0]))]
    columns = [columns[i][::-1] for i in range(len(columns))]
    print columns

    sec = []
    for i in columns:
        far = ''.join(i).rfind('#')
        other_occ = i.count('#') -1
        time = far - other_occ
        sec.append(time)
    shortest = min(sec)
    ANS = []
    for i in range(len(sec)):
        if sec[i] == shortest:
            ANS.append(i)
    return ANS
