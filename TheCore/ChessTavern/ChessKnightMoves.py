def chessKnightMoves(cell):
    o = ord(cell[0])
    l = [chr(o + x) for x in [-2, -1, 1, 2] if 97 <= (o + x) <= 104]
    num = int(cell[1])
    n = [num + x for x in [-2,-1,1,2] if 1<= (num+x) <= 8]
    return (len(l)*len(n))/2
