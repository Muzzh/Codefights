def christmasTree(levelNum, levelHeight):
    first_lines = [5+2*(x) for x in range(levelNum)]
    max_line_lenght = 5 + (levelNum -1)*2 + 2*(levelHeight-1)
    tree_spaces = [" " * x for x in range(levelNum)]
    tree_spaces = tree_spaces[::-1]
    print tree_spaces


    def builder(first_line, levelHeight):
        level = []
        ast_lines = [first_line + 2*x for x in range(levelHeight)]
        spaces = [" " * x for x in reversed(range(levelHeight))]
        for i in range(len(ast_lines)):
            to_add = spaces[i] + ast_lines[i] * "*"
            level.append(to_add)
        return level

    tree = [levelHeight*" " + tree_spaces[0] + " " + "*", levelHeight*" " + tree_spaces[0] + " " + "*", levelHeight*" " + tree_spaces[0] + "***"]

    for i in range(len(first_lines)):
        temp = builder(first_lines[i], levelHeight)
        level = []
        for j in range(len(temp)):
            to_add = tree_spaces[i] + temp[j]
            level.append(to_add)
        for i in level:
            tree.append(i)
    print levelHeight, levelHeight/2, levelHeight-levelHeight/2, levelNum
    if levelHeight%2 == 0:
        to_add = " "*((levelHeight-levelHeight/2) +levelNum) + (levelHeight+1) * "*"
        for i in range(levelNum):
            tree.append(to_add)
    else:
        to_add = " "*((levelHeight-levelHeight/2) +levelNum) + (levelHeight) * "*"
        for i in range(levelNum):
            tree.append(to_add)
    return tree




        
