def shuffledArray(shuffled):

    for i in range(len(shuffled)):
        if sum(shuffled[:i]) + sum(shuffled[i:]) - shuffled[i] == shuffled[i]:
            del shuffled[i]
            return sorted(shuffled)
