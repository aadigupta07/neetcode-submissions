import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(len(original)):
            graph[original[i]].append((cost[i], changed[i]))
        

        total = 0
        dist = defaultdict(lambda: float('inf'))
        completed = {}

        for i in range(len(source)):
            if (source[i], target[i]) in completed:
                total+= completed[(source[i], target[i])]
                continue
            heap = [(0, source[i])]
            dist = defaultdict(lambda: float('inf'))
            dist[source[i]] = 0

            while heap:
                d, node = heapq.heappop(heap)

                if d > dist[node]:
                    continue
                
                if node == target[i]:
                    break
                
                for weight, nei in graph[node]:
                
                    new_dist = dist[node] + weight
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))
            
            if dist[target[i]] == float('inf'):
                return -1
            else:
                total+=dist[target[i]]
                completed[(source[i], target[i])] = dist[target[i]]
        return total




        
