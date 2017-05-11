def squareDigitsSequence(a0):
    elem = [a0]
    added = 0

    def sum_of_sq(num):
        bases = [int(x) for x in str(num)]
        print bases
        to_add = 0
        for i in range(len(bases)):
            to_add += bases[i]**2
        return to_add

    while added < 50:
        to_add = sum_of_sq(elem[-1])
        if to_add in elem:
            break
        else:
            elem.append(to_add)
        added+=1
    return len(elem) + 1
