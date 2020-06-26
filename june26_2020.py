class Solution:
    
    nums = []    
    def __init__(self):
        self.nums = []
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.traverse(root,0)
        return sum(self.nums)
        
    def traverse(self,cnode,value):
        if cnode is None:
            self.nums.append(value)
            return
        
        if cnode.left is None and cnode.right is None:
            self.nums.append(cnode.val + (value*10))
            return
        
        if cnode.left is not None:
            self.traverse(cnode.left,(value*10)+cnode.val)
        
        if cnode.right is not None:
            self.traverse(cnode.right,(value*10)+cnode.val)
            
        return