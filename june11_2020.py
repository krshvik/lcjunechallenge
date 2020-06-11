class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0 
        c = 0 
        for n in nums:
            if n == 0:
                a = a + 1
            else:
                if n == 1:
                    b = b + 1
                else:
                    c = c + 1
        i = 0 
        j = 0 
        while j < a:
            nums[i] = 0
            i = i + 1
            j = j + 1 
        j = 0 
        while j < b:
            nums[i] = 1
            j = j + 1
            i = i + 1
        j = 0 
        while j < c:
            nums[i] = 2
            j = j + 1
            i = i + 1 
        return 