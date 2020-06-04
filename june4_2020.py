class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lens = len(s)-1
        i = 0 
        while i < lens:
            c = s[i]
            s[i] = s[lens]
            s[lens] = c
            i = i + 1
            lens = lens-1
        return 