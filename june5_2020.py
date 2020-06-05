import math 
from random import randint

class Solution:
    
    arr = []
    lena = 0 
    
    def __init__(self, w: List[int]):
        i = 0 
        self.arr = []
        mini = min(w)
        w2 = []
        half = int(mini//2)
        for wi in w:
            val = int(wi//mini)
            if wi - (val*mini) > half:
                val = val + 1                
            w2.append(val)
        for wi in w2:
            v = 0 
            while v < wi:
                self.arr.append(i)
                v = v + 1 
            i = i + 1         
        self.lena = len(self.arr)
        # print(self.arr)
        
    def pickIndex(self) -> int:
        return self.arr[randint(0,self.lena-1)]