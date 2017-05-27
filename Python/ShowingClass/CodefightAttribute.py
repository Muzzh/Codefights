class CodeFighter(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name

    def __getattr__(self,attr):
        return '%s attribute is not defined' %attr


def codefighterAttribute(attribute):
    codefighter = CodeFighter("annymaster", "1234567", "1500", "anny")
    return getattr(codefighter, attribute)
