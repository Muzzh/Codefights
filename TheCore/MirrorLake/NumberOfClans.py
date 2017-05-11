def numberOfClans(divisors, k):
    clans = set()

    for i in range(1, k+1):
        dividable = []
        for j in range(len(divisors)):
            if i%divisors[j] == 0:
                dividable.append(divisors[j])
        dividable = tuple(dividable)
        clans.add(dividable)

    return len(clans)
