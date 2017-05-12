def chessTriangle(n, m):
    init = [[x, y] for x in range(n) for y in range(m)]
    k_moves = [[x,y] for x in [-2,-1,1,2] for y in [-2,-1,1,2] if abs(x) != abs(y)]
    k_poss = []
    print k_poss
    for i in range(len(init)):
        to_add = [[init[i][0] + k_moves[x][0], init[i][1] + k_moves[x][1]] for x in range(len(k_moves)) if 0 <= init[i][0] + k_moves[x][0] < n and 0<= init[i][1] + k_moves[x][1] <m]
        if len(to_add) > 0:
            for i in to_add:
                if i not in k_poss:
                    k_poss.append(i)
    print k_poss
