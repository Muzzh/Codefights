def tennisSet(score1, score2):
    if max(score1,score2) == 6 and min(score1,score2) < 5:
        return True
    if max(score1,score2) == 7 and min(score1,score2) in (5,6):
        return True
    return False
