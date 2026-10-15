class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[1], time[2]))
        

        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
        
        
        result = max(dist[1:])
        return -1 if result == float('inf') else result
