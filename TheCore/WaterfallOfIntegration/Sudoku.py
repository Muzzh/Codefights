def sudoku(grid):
    for i in grid:
        for j in i:
            if i.count(j) > 1:
                return False
    flip = [[grid[x][y] for x in range(9)] for y in range(9)]
    for i in flip:
        for j in i:
            if i.count(j) >1:
                return False
    split = [[(grid[i][:3]), (grid[i][3:6]), (grid[i][6:])] for i in range(9)]
    squ = []
    for i in range(0,9,3):
        for j in range(0,3):
            to_add = [split[i][j]] + [split[i+1][j]] + [split[i+2][j]]
            squ.append(to_add)
    for i in squ:
        i = sum(i, [])
        if sum(i) != 45:
            return False
    return True
