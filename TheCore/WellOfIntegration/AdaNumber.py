def adaNumber(line):
    new_line = []
    for i in range(len(line)):
        if line[i] == '_':
            pass
        if line[i].isdigit() == True:
            pass
        if line[i] == '#':
            new_line = [line[:i], line[i:]]
            break
    if len(new_line) == 2:
        print new_line[0], type(new_line[0])
        if 2 <= int(new_line[0]) <= 16:
            pass
        else:
            return False
        if new_line[1].count('#') != 2:
            return False
        if new_line[1][0] != '#' and new_line[1][len(new_line[1])] != '#':
            return False
        new_line[1] = str(new_line[1])
        for i in range(1, len(new_line[1])-1):
            print i, new_line[1][i]
#            new_line[1][i] = str(new_line[1][i])
            if new_line[1][i].isalnum() == True:
                pass
            else:
                return False
    return True
