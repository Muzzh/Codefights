def rowsRearranging(matrix):
    m = sorted(matrix)
    col = [[m[x][y] for x in range(len(m))] for y in range(len(m[0]))]
    for i in range(len(col)):
        for j in range(len(col[i])-1):
            if col[i][j+1] > col[i][j]:
                pass
            else:
                return False
    return True
