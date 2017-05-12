def treeBottom(tree):
    deep = 0
    deepest = 0
    #find the deepest nested parentesis
    for i in range(len(tree)):
        if tree[i] == '(':
            deep += 1
        if tree[i] == ')':
            if deep > deepest:
                deepest = deep
            deep -= 1
    # deepest is always empty so
    deepest -= 1
    nums = []
    for i in range(len(tree)):
        if tree[i] == '(':
            deep += 1
            if deep == deepest and tree[i+1].isdigit() == True:
                to_add = re.findall('\d+(?= \()', tree[i+1:])[0]
                print to_add
                nums.append(int(to_add))
        if tree[i] == ')':
            deep -= 1
    return nums

    
