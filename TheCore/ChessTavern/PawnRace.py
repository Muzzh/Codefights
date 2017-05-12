def pawnRace(wh, bl, move):
    if wh[0] == bl[0] and int(wh[1]) < int(bl[1]):
        return 'draw'
    if wh[1] == '8' and bl[1] == '1':
        if move == 'w': return 'white'
        else: return 'black'
    if wh[1] == '8': return 'white'

    if bl[1] == '1': return 'black'
    capture = False
    if ord(wh[0]) in [ord(bl[0]) -1, ord(bl[0]) + 1]:
        capture = True

    def shortest(path):
        if path >= 6:
            return path - 1
        return path
    if capture == False or int(wh[1]) >= int(bl[1]):
        wh_path = 8 - int(wh[1])
        bl_path = int(bl[1]) - 1
        winner = 'black'
        if move == 'w':
            if shortest(wh_path) <= shortest(bl_path):
                winner = 'white'
        else:
            if shortest(bl_path) > shortest(wh_path):
                winner = 'white'
        return winner
    else:
        if int(wh[1]) == 1 and int(bl[1]) == 8:
            if move == 'w': return 'black'
            if move == 'b': return 'white'
        elif int(wh[1]) == 1 and int(bl[1]) == 7:
            return 'black'
        elif int(wh[1]) == 2 and int(bl[1]) == 8:
            return 'white'
        elif int(wh[1]) == 2 and int(bl[1]) == 7:
            if move == 'w': return 'black'
            if move == 'b': return 'white'
        else:
            if move == 'w':
                if int(wh[1]) < 3 and 3 < int(bl[1]) < 7:
                    return 'white'
                elif (int(bl[1]) - int(wh[1]))%2 == 0: return 'black'
                else: return 'white'
            else:
                if 2 < int(wh[1]) < 6 and int(bl[1]) > 6:
                    return 'black'
                elif (int(bl[1]) - int(wh[1]))%2 == 0: return 'white'
                else: return 'black'
