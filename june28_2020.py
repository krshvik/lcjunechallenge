class Solution:
    
    routes = []
    
    def __init__(self):
        self.routes = []
    
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        f = {}
        for t in tickets:
            a = t[0]
            b = t[1]
            if a in f:
                f[a].append(b)
            else:
                f[a] = {}
                f[a] = [b]
        for fi in f:
            f[fi].sort()
            
        self.find('JFK',f,'JFK')
        return list(min(self.routes).split())
        
    def find(self,curr,t,route):
        
        if len(t) == 0:
            self.routes.append(route)
            return 
        
        if len(t) == 1:
            if curr not in t:
                return
            if len(t[curr]) > 1:
                return 
            route = route + ' ' + min(t[curr])
            self.routes.append(route)
            return 
        
        if curr not in t:
            return
        
        if len(self.routes) > 0: 
            return 
        
        arr = t[curr]
        lena = len(arr)
        i = 0 
        while i < lena:
            if lena == 1:
                del t[curr]
                self.find(arr[i],t,route+' ' + arr[i])
                t[curr] = arr
            else:
                t[curr] = arr[:i] + arr[i+1:]
                self.find(arr[i],t,route+ ' ' + arr[i])
                t[curr] = arr
            i = i + 1 
        return 
