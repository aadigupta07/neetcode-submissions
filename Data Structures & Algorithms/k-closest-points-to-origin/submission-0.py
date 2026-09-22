class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap, [0-(points[i][0]**2 + points[i][1]**2), points[i][0], points[i][1]])
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [(x,y) for i,x,y in heap]