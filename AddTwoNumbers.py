# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst1 = ""
        lst2 = ""
        
        head = l1
        while head:
            lst1 = lst1 + str(head.val)
            head = head.next
            
        head = l2
        while head:
            lst2 = lst2 + str(head.val)
            head = head.next
            
        s = str(int(lst1[::-1]) + int(lst2[::-1]))
        s = s[::-1]
        
        l3 = ListNode(int(s[0]))
        head = l3
        for i in range(1, len(s)):
            head.next = ListNode(int(s[i]))
            head = head.next
                                 
        return l3
