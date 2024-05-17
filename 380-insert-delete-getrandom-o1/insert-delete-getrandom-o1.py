import random
class RandomizedSet(object):

    def __init__(self):
        self.array =[]
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.array :
            return False
        else :
            self.array.append(val)
            return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.array :
            self.array.remove(val)
            return True
        else :
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()