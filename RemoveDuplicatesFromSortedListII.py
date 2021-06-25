# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = None
        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:  
                    fast = fast.next  # if fast.val == fast.next.val, keep moving fast until those are not equal
                if not slow: # if slow is None, means we remove from first node. so we need to change head
                    head = fast.next
                else:
                    slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
            
        return head
