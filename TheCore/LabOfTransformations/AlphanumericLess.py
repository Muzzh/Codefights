def alphanumericLess(s1, s2):
    import re
    s1, s2 = str(s1), str(s2)
    s1 = re.findall('(\d+|\D+)', s1)
    s2 = re.findall('(\d+|\D+)', s2)

    s1_tokens = []
    s2_tokens = []

    for i in range(len(s1)):
        if s1[i][0].isdigit() == True:
            s1_tokens.append(s1[i])
        else:
            for j in range(len(s1[i])):
                s1_tokens.append(s1[i][j])
    for i in range(len(s2)):
        if s2[i][0].isdigit() == True:
            s2_tokens.append(s2[i])
        else:
            for j in range(len(s2[i])):
                s2_tokens.append(s2[i][j])

    couples = [[s1_tokens[i], s2_tokens[i]] for i in range(len(s1_tokens))]


    same_int = []
    for i in range(len(couples)):

        if len(couples[i]) != 2:
            return len(s1_tokens) < len(s2_tokens)
        if couples[i][0].isalpha() == True:
            if couples[i][0] > couples[i][1]:
                return False
        else:
            if couples[i][1].isalpha() == True:
                if couples[i][0] > couples[i][1]:
                    return False
            if couples[i][0].isdigit() == True and couples[i][1].isdigit() == True:
                if int(couples[i][0]) == int(couples[i][1]):
                    same_int.append(True)
                else:
                    same_int.append(False)
                    if int(couples[i][0]) > int(couples[i][1]):
                        return False

    if all(same_int) == True:
        for i in range(len(couples)):
            if couples[i][0].isdigit() == True and couples[i][1].isdigit() == True:
                if len(couples[i][0]) < len(couples[i][1]):
                    return False
            else:
                pass
    return True
     
