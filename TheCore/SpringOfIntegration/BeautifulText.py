def beautifulText(s, l, r):
#    if r > len(s):
#        return 1
    poss = False
    for i in range(l, r+1):
        if len(s)%i +1 == len(s)/i:
            this_i_poss = False
            poss = True
            to_swap = i
            print to_swap, len(s)/to_swap
            for j in range(0, len(s)/to_swap-1):
                print s[j + (j+1)*to_swap], j, j+ (j+1)*to_swap
                if s[j + (j+1)*to_swap] == ' ':
                    this_i_poss = True
                else:
                    this_i_poss = False
                    poss = False
                    break
            if this_i_poss == True:
                return True
    if poss == False:
        return False
    return True
