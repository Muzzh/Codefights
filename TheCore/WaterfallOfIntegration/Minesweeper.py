def minesweeper(matrix):
    N, M = len(matrix), len(matrix[0])
    def neighbours(i, j):
        return sum(matrix[ii][jj] for ii in range(i-1, i+2) if 0 <= ii < N
                                  for jj in range(j-1, j+2) if 0 <= jj < M
                                  if i != ii or j != jj)
    return [[neighbours(i, j) for j in range(M)] for i in range(N)]
