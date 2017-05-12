def electionsWinners(votes, k):
    to_win = max(votes) + 1
    potential = 0
    for i in range(len(votes)):
        if votes[i] + k >= to_win:
            potential += 1
    if votes.count(max(votes)) == 1 and potential == 0:
        return 1
    return potential
