class Solution:
    
    di = {}
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 or n == 1:
            return 1
        
        if m in self.di:
            if n in self.di[m]:
                return self.di[m][n]
        val = 0 
        
        if m > 1:
            val1 =  self.uniquePaths(m-1,n)
            if m-1 not in self.di:
                self.di[m-1] = {}
            self.di[m-1][n] = val1
            val = val + val1 
        
        if n > 1:
            val2= self.uniquePaths(m,n-1)
            if m not in self.di:
                self.di[m] = {}
            self.di[m][n-1] = val2
            val = val + val2
        
        if m not in self.di:
            self.di[m] = {}
        self.di[m][n] = val 
        
        return val 