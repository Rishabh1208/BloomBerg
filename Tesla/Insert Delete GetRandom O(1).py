from random import choice


class RandomizedSet():
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val):
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.numList)
        self.numList.append(val)
        return True

    def remove(self, val):
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        value = self.numList[-1]
        self.numList[idx] = value
        self.numList.pop()
        self.numMap[value] = idx
        del self.numMap[val]
        return True

    def getRandom(self):
        return choice(self.numList)
