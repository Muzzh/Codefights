def crossingSum(matrix, a, b):
    a_sum = sum(matrix[a])
    b_sum = sum([matrix[x][b] for x in range(len(matrix))])
    return a_sum + b_sum - matrix[a][b]
