class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        di = {}
        for n in nums:
            if n in di:
                return n
            else:
                di[n] = 1
        return -1