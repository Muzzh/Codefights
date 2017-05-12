def polygonPerimeter(m):
    para = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == True:
                if i == 0 or m[i-1][j] == False:
                    para += 1
                if i == len(m) -1 or m[i+1][j] == False:
                    para += 1
                if j == 0 or m[i][j-1] == False:
                    para += 1
                if j == len(m[i]) -1 or m[i][j+1] == False:
                    para += 1
    return para
