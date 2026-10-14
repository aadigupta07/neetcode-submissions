class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # potentially process the nodes with union, and just keep tracking the most recent false union
        n = len(edges)
        parent = [0] * (n+1) # just ignoring index 0
        size = [1] * (n+1) # just ignoring index 0

        for i in range(1, n+1):
            parent[i] = i
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: # already connected
                return False

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            return True
        
        result = []

        for edge in edges:
            if not union(edge[0], edge[1]):
                result = edge
        
        return result
        

        