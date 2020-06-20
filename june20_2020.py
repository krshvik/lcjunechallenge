import math 
class Solution:
        
    def getPermutation(self, n: int, k: int) -> str:
        narr = []
        self.found = k 
        i = 1
        while i <= n:
            narr.append(i)
            i = i + 1
        
        res = ''
            
        ki = 0 
        while k > 1:
            kfact = 0
            lenn = len(narr)-1
            val = math.factorial(lenn)
            i = 0 
            while kfact + val < k:
                kfact = kfact + val
                i = i + 1
            print(res,narr,k,kfact,i)
            res = res + str(narr[i])
            narr = narr[:i] + narr[i+1:]
            k = k - kfact  
        for ni in narr:
            res = res + str(ni)
        return res 
        
            
