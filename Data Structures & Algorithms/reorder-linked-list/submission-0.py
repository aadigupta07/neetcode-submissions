# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        p1 = head
        prev = None
        curr = slow.next
        slow.next = None # this severs first half from second so u dont get a 3 -> 4 -> 3 type of thing after reversing 4 to point at 3

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        p2 = prev
        
        while p2:
            p1_next = p1.next 
            p2_next = p2.next   

            p1.next = p2          
            p2.next = p1_next 

            p1 = p1_next 
            p2 = p2_next
        








