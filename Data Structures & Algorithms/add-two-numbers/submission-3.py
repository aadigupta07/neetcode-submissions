# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        sum_list = dummy
        carry = 0
        while l1 and l2:
            value = l1.val+l2.val+carry
            sum_list.next = ListNode((l1.val + l2.val + carry)%10, None)
            if value > 9: # moving carry calculation to after creating node
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            sum_list = sum_list.next

        while l1:
            
            sum_list.next = ListNode((l1.val + carry)%10, None)
            if l1.val + carry > 9:
                carry = 1
            else:
                carry = 0
            sum_list = sum_list.next
            l1 = l1.next

        while l2:
            
            sum_list.next = ListNode((l2.val + carry)%10, None)
            if l2.val + carry > 9:
                carry = 1
            else:
                carry = 0
            sum_list = sum_list.next
            l2 = l2.next
        
        if carry == 1:
            sum_list.next = ListNode(1, None)
        return dummy.next
