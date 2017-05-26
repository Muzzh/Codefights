def isTestSolvable(ids, k):
    digitSum = lambda x: sum(int(str(x)[y]) for y in range(len(str(x))))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
