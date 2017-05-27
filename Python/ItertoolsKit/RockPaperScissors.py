from itertools import permutations

def rockPaperScissors(players):
    return list(permutations(sorted(players),2))
