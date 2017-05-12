def firstOperationCharacter(expr):
    deep = 0
    deepest = 0
    expr = str(expr)
    for i in range(len(expr)):
        if expr[i] not in ['(', ')']:
            pass
        elif expr[i] == '(':
            deep+=1
        else:
            if deep >= deepest:
                deepest = deep
            deep -= 1
    end_index = []
    for i in range(len(expr)):
        if expr[i] not in ['(', ')']:
            pass
        elif expr[i] == '(':
            deep+=1
        elif expr[i] == ')':
            print deep
            if deep == deepest:
                end_index.append(i)
            deep -= 1
        print expr[i], deep
    print end_index
    if len(end_index) == 0:
        if '*' in expr:
            return expr.find('*')
        else:
            return expr.find('+')
    ranges = []
    for i in end_index:
        for j in range(i, -1, -1):
            if expr[j] == '(':
                to_add = [[j,i],[expr[j:i+1]]]
                ranges.append(to_add)
                break
            else: pass
    mult = []
    for i in range(len(ranges)):
        if '*' in str(ranges[i][1]):
            ind = str(ranges[i][1]).index('*')
            return ind + ranges[i][0][0] -2
    for i in range(len(ranges)):
        if '+' in str(ranges[i][1]):
            ind = str(ranges[i][1]).index('+')
            return ind + ranges[i][0][0] -2
    while deepest > 0:
        deepest -= 1
        for i in range(len(expr)):
            if expr[i] not in ['(', ')']:
                pass
            elif expr[i] == '(':
                deep+=1
            elif expr[i] == ')':
                if deep == deepest:
                    end_index.append(i)
                deep = 0
        if len(end_index) == 0:
            if '*' in expr:
                return expr.find('*')
            else:
                return expr.find('+')
        ranges = []
        for i in end_index:
            for j in range(i, -1, -1):
                if expr[j] == '(':
                    to_add = [[j,i],[expr[j:i+1]]]
                    ranges.append(to_add)
                    break
                else: pass
        mult = []
        for i in range(len(ranges)):
            if '*' in str(ranges[i][1]):
                ind = str(ranges[i][1]).index('*')
                return ind + ranges[i][0][0] -2
        for i in range(len(ranges)):
            if '+' in str(ranges[i][1]):
                ind = str(ranges[i][1]).index('+')
                return ind + ranges[i][0][0] -2
        
