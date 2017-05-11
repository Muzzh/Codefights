def rounders(value):
    dig = [int(x) for x in str(value)]
    for i in range(len(dig)-1, 0, -1):
        if dig[i] >= 5:
            dig[i-1] += 1
        dig[i] = 0
    return int(''.join([str(x) for x in dig]))
