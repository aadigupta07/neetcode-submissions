class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        min_heap = []

        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num)) # pushing freq, num backwards to iteration from enumerate

            if (len(min_heap) > k):
                heapq.heappop(min_heap)
        
        return [num for freq, num in min_heap] # return list of only nums
        