import random

def createDie(seed, n):
    class Die(object):
        def __new__(self, seed, n):
            self.seed = seed
            self.n = n
            random.seed(self.seed)
            self.res = int((random.random()*self.n) +1)
            return self.res


    class Game(object):
        die = Die(seed, n)

    return Game.die
