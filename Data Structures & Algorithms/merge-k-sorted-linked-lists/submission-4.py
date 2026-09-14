# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # technically meant to keep merging two lists at a time and use O(1) space but this is honestly better
        dummy = ListNode(0, None)
        result = dummy
        n = len(lists)
        heap = []

        counter = 0
        for i in range(n): # prepopulate
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, counter, lists[i])) # counter for tie breaker so it doesn't try to sort by node (not possible)
                counter +=1
        
        if not heap:
            return None


        while heap: 
            curr = heapq.heappop(heap)[2] 
            result.next = curr
            result = result.next

            if curr.next: # push replacement from list (so u can always find minimum from available nodes to push)
                heapq.heappush(heap, (curr.next.val, counter, curr.next))
                counter +=1


        return dummy.next