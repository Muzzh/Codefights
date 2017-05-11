def differentSquares(matrix):
    squares = set()
    for c in range(len(matrix)-1):
        for r in range(len(matrix[0])-1):
            squares.add((matrix[c][r], matrix[c][r+1], matrix[c+1][r], matrix[c+1][r+1])
    return len(squares)
