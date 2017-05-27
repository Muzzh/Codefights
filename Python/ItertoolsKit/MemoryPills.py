from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda x: len(x)%2 == 1, pills + ['','',''])
    next(gen)
    return [next(gen) for _ in range(3)]
