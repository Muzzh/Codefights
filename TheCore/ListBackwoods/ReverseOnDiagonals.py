def reverseOnDiagonals(matrix):
    f_diag = [matrix[x][x] for x in range(len(matrix))]
    s_diag = [matrix[x][len(matrix)-1-x] for x in range(len(matrix))]
    f_diag = f_diag[::-1]
    s_diag = s_diag[::-1]

    for i in range(len(f_diag)):
        matrix[i][i] = f_diag[i]
    for i in range(len(s_diag)):
        matrix[i][len(matrix)-1-i] = s_diag[i]
    return matrix
