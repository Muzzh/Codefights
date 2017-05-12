def swapDiagonals(matrix):
    a = [matrix[x][x] for x in range(len(matrix))]
    b = [matrix[x][len(matrix)-1-x] for x in range(len(matrix))]
    f_diag = b
    s_diag = a

    for i in range(len(f_diag)):
        matrix[i][i] = f_diag[i]
    for i in range(len(s_diag)):
        matrix[i][len(matrix)-1-i] = s_diag[i]
    return matrix
