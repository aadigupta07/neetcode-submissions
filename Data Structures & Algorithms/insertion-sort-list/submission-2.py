# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        3, 1, 2

        dummy = ListNode(float('-inf'), None)

        while head:
            # detach head
            curr = head
            head = head.next
            

            prev = dummy
            temp = dummy.next
            while temp and temp.val < curr.val: # loop stops when end is hit, or temp.val > curr.val
                prev = temp
                temp = temp.next
            
            prev.next = curr
            curr.next = temp
            
        return dummy.next

        