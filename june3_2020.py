class Solution:
    
    dist_len = 0 
    di = {}
    
    def __init__(self):
        self.dist_len = 0 
        self.di= {}
        
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0 
        if len(costs) == 2:
            return min(costs[0][0] + costs[1][1],costs[0][1] + costs[1][0])
        
        self.dist_len = int(len(costs)//2)
        value =  self.two(costs,0,0)
        return value 
    
    def two(self,costs,alen,blen):
        
        if alen in self.di and blen in self.di[alen]:
            return self.di[alen][blen]

        if alen not in self.di:
            self.di[alen] = {}
        
        tcost = 0 
        
        if alen == self.dist_len:
            for c in costs:
                tcost = tcost + c[1]
            self.di[alen][blen] = tcost 
            return tcost 
        
        if blen == self.dist_len:
            for c in costs:
                tcost = tcost + c[0]
            self.di[alen][blen] = tcost 
            return tcost ## acost + bcost 
        
        
        
        cost1 = self.two(costs[1:],alen+1,blen)
        
        if alen+1 not in self.di:
            self.di[alen+1]  = {}
        self.di[alen+1][blen] = cost1
        
        cost2 = self.two(costs[1:],alen,blen+1)
        
        self.di[alen][blen+1] = cost2 
        
        val = min(cost1+costs[0][0],cost2+costs[0][1])
        
        self.di[alen][blen] = val
        return val 
    
