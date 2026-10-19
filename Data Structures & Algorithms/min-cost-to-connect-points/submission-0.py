class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                point1 = points[i]
                point2 = points[j]
                dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

                edges.append([i, j, dist])
        
        edges.sort(key = lambda edge: edge[2])
        
        parent = list(range(len(points)))
        size = [1] * len(points)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            size[rootA] += size[rootB]
            parent[rootB] = rootA
            return True
        
        total = 0
        count = 0
        for start, end, weight in edges:
            if union(start, end):
                total+=weight
                count+=1
            
            if count == len(points) - 1:
                return total
        
        return total
            





