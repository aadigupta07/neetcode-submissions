class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        
        for _ in range(k+1):
            copy = dist.copy()

            for start, end, price in flights:
                if dist[start] == float('inf'):
                    continue
                
                copy[end] = min(dist[start] + price, copy[end])
            
            dist = copy



        return -1 if dist[dst] == float('inf') else dist[dst]