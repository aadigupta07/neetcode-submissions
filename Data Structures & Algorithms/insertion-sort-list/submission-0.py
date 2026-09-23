class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'), None)
        
        curr = head
        while curr:
            next_temp = curr.next  # save this BEFORE we detach curr
            
            # find the insertion point: the last node in the sorted list
            # whose value is <= curr.val
            insertion = dummy
            while insertion.next and insertion.next.val < curr.val:
                insertion = insertion.next
            
            # splice curr in right after `insertion`
            curr.next = insertion.next
            insertion.next = curr
            
            curr = next_temp  # move on to the next original node
        
        return dummy.next