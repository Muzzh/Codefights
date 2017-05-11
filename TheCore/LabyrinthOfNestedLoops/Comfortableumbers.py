def comfortableNumbers(L, R):
    couples = 0

    def s(a):
        comfy_range = sum(int(x) for x in str(a))
        return comfy_range

    for i in range(L, R+1):
        for j in range(i+1,R+1):
            if j > i+s(i): break
            if i < j-s(j): break
            if i-s(i) <= j <= i+s(i) and j-s(j) <= i <= j+s(j):
                couples += 1

    return couples
