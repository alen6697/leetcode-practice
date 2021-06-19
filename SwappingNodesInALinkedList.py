# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = head
        length = 0
        tail = None
        while start:
            length = length + 1
            if length == k:
                tail = start
            start = start.next
        
        count = 0
        start = head
        while count < length - k:
            count = count + 1
            start = start.next
            
        tmp = start.val
        start.val = tail.val
        tail.val = tmp
        
        return head
