class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [0] * n
        size = [1] * n
        for i in range(n):
            parent[i] = i
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: # check if they already in union
                return False
            
            if size[rootA] < size[rootB]:
                rootA, rootB, = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            return True
        
        for edge in edges:
            if union(edge[0], edge[1]):
                n-=1
        
        return n
        
        
