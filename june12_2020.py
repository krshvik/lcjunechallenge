import random

class RandomizedSet:
    
    di = {}
    arr = []
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.di = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.di:
            self.di[val] = 1 ## len(self.arr)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.di:
            ind = self.di[val]
            del self.di[val]
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        arr = list(self.di)
        lenn = len(arr)
        return arr[random.randint(0,lenn-1)]
        
