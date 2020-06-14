class Solution:
    
    pr = {}
    found = {}
    
    def __init__(self):
        self.found = {}
        self.pr = {}
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        for f in flights:
            s = f[0]
            d = f[1]
            p = f[2]
            
            if s not in self.pr:
                self.pr[s] = {}
            
            self.pr[s][d] = p
        
        value = self.find(src,dst,K+1)
        print(self.pr)
        print(self.found)
        return value 
        
        
    def find(self,src,dst,stops):
        
        if stops < 0:
            return -1 
        
        if stops == 0:
            if src == dst:
                return 0
            return -1 

        if src == dst:
            return 0 

        
        if src not in self.pr:
            return -1
        
        
        if src in self.found and dst in self.found[src] and stops in self.found[src][dst]:
            return self.found[src][dst][stops]
        
        mprice = 99999999999999999999
        
        for f in self.pr[src]:
            p1 = self.find(f,dst,stops-1)
            if p1 != -1 and p1 + self.pr[src][f] < mprice:
                mprice = p1 + self.pr[src][f]
        
        if src not in self.found:
            self.found[src] = {}
            
        if dst not in self.found[src]:
            self.found[src][dst] = {}
        
        if mprice != 99999999999999999999:
            self.found[src][dst][stops] = mprice
            return mprice
        
        self.found[src][dst][stops] = -1
        return -1 
