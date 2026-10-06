class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sorted will give duplicate values
        # the idea of starting at the first value guarantees you creating a group, since it has to be part of some group
        # main concern is pulling out respective values, and going to the next smallest after
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            if count[heap[0]] <= 0:
                heapq.heappop(heap)
                continue
            curr = heapq.heappop(heap)
            weight = count[curr]
            for i in range(curr+1, curr+groupSize):
                if count[i] < weight:
                    return False
                else:
                    count[i]-= weight
        
        return True
                    
        
        



