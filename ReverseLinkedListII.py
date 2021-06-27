# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        
        dummy = ListNode(0, next=head)
        prev = dummy
        i = 1
        while i < left:
            prev = prev.next # prev stop in previous of left 
            i = i + 1
            
        cur = prev.next  # cur point to left
        nx = cur.next  # nx porint to next of left
        
        while i < right:
            tmp = nx.next  # tmp point to nx.next because we want to store nx.next
            nx.next = cur  # reverse cur.next to point to cur
            cur = nx  # shift cur to next one
            nx = tmp
            i = i + 1
            
        prev.next.next = nx
        prev.next = cur
        
        return dummy.next
