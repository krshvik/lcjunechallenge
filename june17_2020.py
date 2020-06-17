class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cannot = {}
        
        if board == []:
            return
        
        lenb = len(board[0])
        i = 0
        c = []
        
        while i < lenb:
            if board[0][i] == 'O':
                c.append([0,i])## = {}
            i = i + 1 
        
        lenb = len(board)
        i = 1 
        
        while i < lenb-1:
            lenb2 = len(board[i])-1
            
            if board[i][0] == 'O':
                c.append([i,0])
            
            if board[i][lenb2] == 'O':
                c.append([i,lenb2])
            
            i = i + 1 
        
        i = 0 
        lenb2 = len(board[lenb-1])
        
        while i < lenb2:
            if board[lenb-1][i] == 'O':
                c.append([lenb-1,i])
            i = i + 1 
        
        print(c)
        while len(c) > 0:
            
            temp = []
            
            for ci in c:
                ro = ci[0]
                co = ci[1]
                
                if ro not in cannot:
                    cannot[ro] = {}
                cannot[ro][co] = 1
                if ro-1 > -1:
                    if board[ro-1][co] == 'O':
                        if ro-1 not in cannot or (ro-1 in cannot and co not in cannot[ro-1]):
                            temp.append([ro-1,co])
                if ro+1 < len(board):
                    if board[ro+1][co] == 'O':
                        if ro+1 not in cannot or (ro+1 in cannot and co not in cannot[ro+1]):
                            temp.append([ro+1,co])
                if co-1 > -1:
                    if board[ro][co-1] == 'O':
                        if ro not in cannot or (ro in cannot and co-1 not in cannot[ro]):
                            temp.append([ro,co-1])
                if co+1 < len(board[ro]):
                    if board[ro][co+1] == 'O':
                        if ro not in cannot or (ro in cannot and co+1 not in cannot[ro]):
                            temp.append([ro,co+1])
            
            c = temp 
            # print(c)
            
        
        lenb = len(board)
        i = 0 
        while i < lenb:
            j = 0 
            lenb2 = len(board[i])
            while j < lenb2:
                if board[i][j] == 'O':
                    if i not in cannot or (i in cannot and j not in cannot[i]):
                        board[i][j] = 'X'
                j = j + 1 
            i = i + 1
        return 
        