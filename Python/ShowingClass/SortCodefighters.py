def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return map(str, res)

    class CodeFighter(object):
        def __init__(self, username, _id, xp):
            self.username = username
            self.id = _id
            self.xp = xp

        def __str__(self):
            return self.username

        def __cmp__(self, other):
            if self.xp < other.xp:
                return 1
            elif self.xp > other.xp:
                return -1
            else:
                if self.id < other.id:
                    return -1
                elif self.id > other.id:
                    return 1
                else:
                    return 0
