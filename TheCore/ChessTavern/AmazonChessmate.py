def amazonCheckmate(k, a):
    board = [str(chr(x) + str(y)) for x in range(97,105) for y in range(1,9)]

    k_threat = [chr(ord(k[0])+x) + str(int(k[1])+y) for x in range(-1,2) for y in range(-1,2)]
    a_col = [str(a[0]+str(y)) for y in range(1,9)]
    a_row = [chr(x) + str(a[1]) for x in range(97,105)]
    f_diag = [chr(ord(a[0]) + x) + str(int(a[1]) + x) for x in range(-7,8) if 97<=ord(a[0]) +x<=104 and 1<=int(a[1]) + x<=8]
    s_diag = [chr(ord(a[0]) + x) + str(int(a[1]) - x) for x in range(-7,8) if 97<=ord(a[0]) +x<=104 and 1<=int(a[1]) - x<=8]
    knight = [chr(ord(a[0]) + x) + str(int(a[1]) + y) for x in range(-2,3) for y in range(-2,3) if (abs(x)+abs(y)) == 3 and 97<=ord(a[0])+x<=104 and 1<=int(a[1]) + y <=8]

    board = [x for x in board if x not in k_threat]
    board = [x for x in board if x != a]

    def remove_hidden(l):
        L = l
        if k in l:
            k_index = l.index(k)
            a_index = l.index(a)
            if k_index < a_index:
                L = list(l[k_index+2:])
            else:
                L = list(l[:k_index-1])
        return L
    a_col = remove_hidden(a_col)
    a_row = remove_hidden(a_row)
    s_diag = remove_hidden(s_diag)
    f_diag = remove_hidden(f_diag)
    a_threat = a_col + a_row + f_diag + s_diag + knight

    for i in range(len(a_threat)-1, -1, -1):
        if a_threat[i] in k_threat and a_threat[i] != a:
            del a_threat[i]

    bk_moves = [[x, y] for x in range(-1,2) for y in range(-1,2) if [x, y] != [0, 0]]

    def escape(bk):
        esc = False
        for i in range(len(bk_moves)):
            move = str(chr(ord(bk[0])+ bk_moves[i][0])) + str(int(bk[1]) + bk_moves[i][1])
            if move not in a_threat and move not in k_threat and 97<=ord(bk[0])+ bk_moves[i][0]<=104 and 1<=int(bk[1]) + bk_moves[i][1]<=8:
                esc = True
        return esc

    checkmate = 0
    check = 0
    stalemate = 0
    safe = 0

    if a not in k_threat:
        a_threat = [x for x in a_threat if x != a]
    print escape('h8')
    for i in range(len(board)):
        esc = escape(board[i])
        if esc == False:
            if board[i] in a_threat:
                checkmate += 1
            else:
                stalemate += 1
        elif esc == True:
            if board[i] in a_threat:
                check += 1
            else:
                safe += 1
    return [checkmate, check, stalemate, safe]





    
