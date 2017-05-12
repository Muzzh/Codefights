def starRotation(matrix, width, center, t):
    import copy
    temp = copy.deepcopy(matrix)
    t = t%8
    def case(t):
        if t == 0:
            return matrix
        if t == 1:
            for i in range(-(width/2), width/2 + 1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]][center[1]+i]
                matrix[center[0]+i][center[1]] = temp[center[0]+i][center[1]+i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]-i][center[1]]
                matrix[center[0]][center[1]+i] = temp[center[0]-i][center[1]+i]
        if t == 2:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]-i][center[1]+i]
                matrix[center[0]+i][center[1]] = temp[center[0]][center[1]+i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]-i][center[1]-i]
                matrix[center[0]][center[1]+i] = temp[center[0]][center[1]+i]
        if t == 3:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]-i][center[1]]
                matrix[center[0]+i][center[1]] = temp[center[0]-i][center[1]-i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]][center[1]-i]
                matrix[center[0]][center[1]+i] = temp[center[0]-i][center[1]-i]
        if t == 4:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]-i][center[1]-i]
                matrix[center[0]+i][center[1]] = temp[center[0]-i][center[1]]
                matrix[center[0]-i][center[1]+i] = temp[center[0]+i][center[1]-i]
                matrix[center[0]][center[1]+i] = temp[center[0]][center[1]-i]
        if t == 5:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]][center[1]-i]
                matrix[center[0]+i][center[1]] = temp[center[0]-i][center[1]-i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]+i][center[1]]
                matrix[center[0]][center[1]+i] = temp[center[0]+i][center[1]-i]
        if t == 6:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]+i][center[1]-i]
                matrix[center[0]+i][center[1]] = temp[center[0]][center[1]-i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]+i][center[1]+i]
                matrix[center[0]][center[1]+i] = temp[center[0]+i][center[1]]
        if t == 7:
            for i in range(-(width/2), width/2 +1):
                matrix[center[0]+i][center[1]+i] = temp[center[0]+i][center[1]]
                matrix[center[0]+i][center[1]] = temp[center[0]+i][center[1]-i]
                matrix[center[0]-i][center[1]+i] = temp[center[0]][center[1]+i]
                matrix[center[0]][center[1]+i] = temp[center[0]+i][center[1]+i]

    case(t)

    return matrix
