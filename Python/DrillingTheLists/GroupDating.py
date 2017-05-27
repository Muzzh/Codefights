def groupDating(male, female):
    return [male[i] for i in range(len(male)) if male[i] != female[i]], [female[i] for i in range(len(female)) if female[i] != male[i]]
