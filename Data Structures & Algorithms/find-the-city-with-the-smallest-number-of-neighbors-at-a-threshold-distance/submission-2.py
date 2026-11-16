class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
        
        minimum = float('inf')
        result = -1
        for city in range(n):
            dist = [float('inf')] * n
            dist[city] = 0
            count = 0

            heap = [(0, city)]

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue
                
                for nei, weight in graph[node]:
                    new_dist = d + weight
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))
            
            for j in range(len(dist)):
                if j != city and dist[j] <= distanceThreshold:
                    count+=1
            
            if count <= minimum:
                minimum = count
                result = city
        
        return result
