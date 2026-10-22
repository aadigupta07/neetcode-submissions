# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        prev = None
        first = head
        second = head.next

        new_head = ListNode(0, second)

        # I want to point first to the second node in next iteration

        1, 2, 3
        1, 2
        

        while second:
            temp = second.next 
            second.next = first

            first.next = temp
            if temp and temp.next:
                first.next = temp.next

            first = second
            second = temp
            
            

            if second:
                first = second
                second = second.next

        

        return new_head.next
            
