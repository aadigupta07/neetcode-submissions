class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for road in roads:
            graph[road[0]].append((road[1], road[2]))
            graph[road[1]].append((road[0], road[2]))

        queue = deque()
        queue.append(1)
        visited = set([1])

        minimum = float('inf')
        while queue:
            curr = queue.popleft()

            for nei, val in graph[curr]:
                minimum = min(minimum, val)
                
                if nei in visited:
                    continue

                queue.append(nei)
                visited.add(nei)

        return minimum

            

        