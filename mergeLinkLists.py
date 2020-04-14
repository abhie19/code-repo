# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)
        new_l = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                new_l.next = l1
                l1 = l1.next
            else:
                new_l.next = l2
                l2 = l2.next
            new_l = new_l.next
        new_l.next = l1 if l1 else l2 # to handle cases where l1 or l2 is smaller and we just add the to the end of new list
        return prehead.next
