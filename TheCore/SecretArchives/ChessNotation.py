def chessNotation(notation):
    n = notation.split('/')
    n = [str(x) for x in n]
    l = []
    for i in n:
        new_i = []
        for j in i:
            if j.isdigit() == False:
                new_i.append(j)
            if j.isdigit() == True:
                add = 0
                while add < int(j):
                    new_i.append('empty')
                    add += 1
        l.append(new_i)
    flip = [[l[x][y] for x in range(len(l)-1,-1,-1)] for y in range(len(l[0]))]
    print flip
    new_flip = []
    for i in range(len(flip)):
        new_i = ''
        num = 0
        for j in range(len(flip[i])):
            if flip[i][j] != 'empty':
                num = 0
                new_i += flip[i][j]
            else:
                index = 0
                while flip[i][j+index] == 'empty' and j + index < len(flip[i]) -1:
                    print index + j, flip[i][j+index], index
                    index += 1
                new_i += str(index+1)

        new_flip.append(new_i)
    print new_flip
    return '/'.join(new_flip)


    
