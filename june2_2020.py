# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = None
        while node.next is not None:
            temp = node
            node.val = node.next.val 
            node = node.next 
        temp.next = None
        return 