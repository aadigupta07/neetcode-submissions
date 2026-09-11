# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head) # u need this in case of edge case where u remove head
        prev = dummy
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        while fast:
            prev = prev.next
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next # if u are removing head (edge case), this also modifies dummy.next since prev never moved from dummy

        
        return dummy.next