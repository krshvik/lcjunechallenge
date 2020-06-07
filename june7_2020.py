class Solution:
    
    di = {}
    def __init__(self):
        self.di = {}
    
    def change(self, amount: int, coins: List[int]) -> int:
        
        if coins == []:
            if amount == 0:
                return 1
            return 0 
        
        if amount == 0:
            print(coins)
            return 1 
        
        
        lenc = len(coins)
        
        if amount in self.di:
            if lenc in self.di[amount]:
                return self.di[amount][lenc]
        
        tote = 0 
        c = coins[0]
        while c <= amount:
            val = self.change(amount-c,coins[1:])
            if val > 0:
                # print(coins[0],amount,val)
                tote = tote + val
            c = c + coins[0]
        val = self.change(amount,coins[1:])
        if val > 0:
            # print(coins[1:],amount,val)
            tote = tote + val
        
        if amount not in self.di:
            self.di[amount] = {}
        
        self.di[amount][lenc] = tote 
        
        return tote 