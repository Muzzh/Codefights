def bishopAndPawn(bishop, pawn):
    return (abs(int(bishop[1]) - int(pawn[1])) - abs(ord(bishop[0]) - ord(pawn[0]))) == 0
