class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_end = dummy   # NEW: tracks node right before current group (renamed from your "prev")
        curr = head

        while curr:
            counter = 0
            temp = curr
            while temp and counter < k:
                temp = temp.next
                counter += 1

            if counter < k:
                break

            group_start = curr   # NEW: save original first node — becomes the tail after reversal

            prev = None           # NEW: local reversal pointer, separate from prev_group_end
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # NEW: stitch the reversed group back into the list
            prev_group_end.next = prev        # prev is now the new head of this reversed group
            group_start.next = curr           # group_start is now the tail; point it to the next group

            prev_group_end = group_start      # NEW: update anchor for the next iteration

        return dummy.next