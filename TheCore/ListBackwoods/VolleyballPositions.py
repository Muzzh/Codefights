def volleyballPositions(formation, k):
    k = k%6
    if k == 0:
        return formation
    positions = [[3,2], [1,2], [0,1], [1,0], [3,0], [2,1]]
    new_pos = []
    for i in range(len(positions)):
        if i < 6 - k:
            new_i = i + k
            new_pos.append(positions[new_i])
        else:
            new_i = i - (6-k)
            new_pos.append(positions[new_i])

    positions_player = []
    for i in range(len(positions)):
        m = positions[i][0]
        n = positions[i][1]
        to_add = formation[m][n]
        positions_player.append(to_add)

    for i in range(len(positions_player)):
        x = new_pos[i][0]
        y = new_pos[i][1]
        to_add = positions_player[i]
        formation[x][y] = to_add
    return formation
