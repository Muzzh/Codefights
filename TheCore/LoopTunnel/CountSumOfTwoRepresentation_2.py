def countSumOfTwoRepresentations2(n, l, r):
    count = 0
    poss = range(l,r+1)
    for i in range(len(poss)):
        for j in range(i,len(poss)):
            if poss[j] + poss[i] == n:
                count +=1
    return count
