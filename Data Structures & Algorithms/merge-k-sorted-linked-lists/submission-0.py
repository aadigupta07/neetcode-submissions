# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        result = dummy
        n = len(lists)
        heap = []

        counter = 0
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, counter, lists[i]))
                counter +=1
        
        if not heap:
            return None


        while heap:
            curr = heapq.heappop(heap)[2]
            next_node = curr.next
            result.next = curr
            result = result.next

            if next_node:
                heapq.heappush(heap, (next_node.val, counter, next_node))
                counter +=1


        return dummy.next