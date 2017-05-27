def fixTree(tree):
    return [tree[i].strip(' ').center(max(len(s) for s in tree)) for i in range(len(tree))]
