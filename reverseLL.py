class Solution:

  def reverseLL(self, head: ListNode)-> ListNode
        # recursive
        # if head is None or head.next is None: return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head
        
        # Iterative 
        # base case
        if not head: return None
        new_head = ListNode(head.val, None)
        head = head.next
        
        while head:
            new_head = ListNode(head.val, new_head)
            head = head.next
            
        return new_head
