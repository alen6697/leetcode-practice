# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        head1 = list1
        tail1 = None
        idx = 0
        while idx != a: # search for index a and make tail1 point to it
            tail1 = head1
            head1 = head1.next
            idx = idx + 1
            
        while idx != b: # search for index b and make head1 point to it
            head1 = head1.next
            idx = idx + 1
        
        head2 = list2
        while head2.next is not None: # find last node of list2
            head2 = head2.next
            
        tail1.next = list2
        head2.next = head1.next
        
        return list1
