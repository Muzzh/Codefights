def seatsInTheater(nCols, nRows, col, row):
    total = 0
    for i in range(row+1, nRows+1):
        for j in range(col, nCols+1):
            total += 1
    return total
