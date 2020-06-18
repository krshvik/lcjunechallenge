class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == []:
            return 0
        lenc = len(citations)
        if lenc == 1:
            if citations[0] >= 1:
                return 1
            return 0
        i = lenc-1
        z = 1 
        chk = 0 
        while chk == 0 and i > -1 and citations[i] > z:
            if i-1 > -1 and citations[i-1] > z: 
                i = i - 1
                z = z + 1
            else:
                chk = 1 
        print(citations[i])
        val = citations[i]
        return min(citations[i],z)