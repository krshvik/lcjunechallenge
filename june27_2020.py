class Solution:
    
    di = {}
    
    def __init__(self):
        self.di = {}
        self.di[1] = 1
        self.di[4] = 1
        self.di[9] = 1 
    
    def numSquares(self, n: int) -> int:
        
        if n in self.di:
            return self.di[n]
        
        mini = 999999999999999
        ns = int(n**0.5)
        
        if ns*ns == n:
            self.di[n] = 1
            return 1 
        
        while ns > 0:
            val = self.numSquares(n-(ns*ns))
            if val + 1 < mini:
                mini = val + 1 
            ns = ns - 1 
        
        self.di[n] = mini
        return mini
            