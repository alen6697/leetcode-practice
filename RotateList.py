# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head
        
        h = head
        length = 0
        while h:
            length = length + 1
            h = h.next
            
        k = k % length
        
        count = 0
        h = head
        tail = head
        while h.next:
            count = count + 1
            if count < length - k:
                tail = tail.next
            h = h.next
            
        h.next = head
        head = tail.next
        tail.next = None
        
        return head
