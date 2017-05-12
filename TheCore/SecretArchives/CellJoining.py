def cellsJoining(table, coords):
    rows = []
    row = 1
    beg = 1
    actual_row = 0
    while row < len(table):
        if table[row][0] != '+':
            row += 1
        else:
            rows.append([beg, row])
            row += 1
            beg = row
    columns = []
    col = 1
    beg = 1
    actual_col = 0
    while col < len(table[0]):
        if table[0][col] != '+':
            col += 1
        else:
            columns.append([beg, col])
            col += 1
            beg = col
    bot = rows[coords[0][0]][1]
    left = columns[coords[0][1]][0]
    top = rows[coords[1][0]][0]
    right = columns[coords[1][1]][1]
    for i in range(top, bot):
        table[i] = table[i][:left] + re.sub(r'\|', ' ', table[i][left:right]) + table[i][right:]
        if table[i][1] == '-':
            table[i] = table[i][:left] + re.sub(r'\+|-', ' ', table[i][left:right]) + table[i][right:]
        if i == 1:
            table[i-1] = table[i-1][:left] + re.sub(r'\+', '-', table[i-1][left:right]) + table[i-1][right:]
        if i +1 == len(table)-1:
            table[i+1] = table[i+1][:left] + re.sub(r'\+', '-', table[i+1][left:right]) + table[i+1][right:]
    if left == 1:
        for i in range(top, bot):
            if table[i][0] == '+':
                table[i] = '|' + table[i][1:]
    if right == len(table[0])-1:
        for i in range(top,bot):
            if table[i][len(table[i])-1] == '+':
                table[i] = table[i][:-1] + '|'
    return table
            
