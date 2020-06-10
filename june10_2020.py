class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        
        return self.search(nums,target,0,len(nums)-1)
        
    def search(self,nums,target,l,r):
        
        if l == r:
            if nums[l] == target:
                return l
            if nums[l] < target:
                return l + 1
            return l 
        
        mid = int((l+r)//2)
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self.search(nums,target,mid+1,r)
        if mid - 1 >= 0:
            if l <= mid-1:
                return self.search(nums,target,l,mid-1)
            return self.search(nums,target,l,l)
        
        return self.search(nums,target,l,0)