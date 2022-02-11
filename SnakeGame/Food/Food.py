from abc import abstractmethod


class Food():
    def __init__(self, pos):
        self.pos = pos
        self.color = 0xff08fc

    def getScore(self):
        return 1