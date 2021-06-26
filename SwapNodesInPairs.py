# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        second = None
        tmp = None
        count = 0
        isFirstSwap = True
        while first != None:
            count = count + 1
            if count == 2:
                count = 0
                if isFirstSwap:
                    head = first
                    isFirstSwap = False
                    
                if tmp != None:
                    tmp.next = first
                second.next = first.next
                first.next = second
                a = first
                first = second
                second = a
                
            tmp = second
            second = first
            first = first.next
            
        return head
