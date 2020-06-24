class Solution:
    
    cache = {}
    
    def numTrees(self, n: int) -> int:
        i = 1
        arr = []
        while i <= n:
            arr.append(i)
            i = i + 1 
        return self.trees(arr)
    
    def trees(self,arr):
        
        if len(arr) in self.cache:
            return self.cache[len(arr)]
        
        if len(arr) <= 1:
            return 1
        if len(arr) == 2:
            return 2
        
        lena = len(arr)-1
        i = 0
        val = 0 
        while i <= lena:
            l = self.trees(arr[:i])
            r = self.trees(arr[i+1:])
            val = val + (l*r)
            i = i + 1 
        self.cache[lena+1] = val 
        return val 