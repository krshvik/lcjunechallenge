class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while len(s) > 0:
            c = s[:1]
            s = s[1:]
            val = t.find(c)
            if val == -1:
                return False
            t = t[val+1:]
        return True 