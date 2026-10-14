class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree is all connected, no cycles
        # check that n is 1? after processing edges with true/false
        # if you just don't subtract if union is false, it should do the deal itself, but you can probably exit early with that check
        if len(edges) != n-1:
            return False
        
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

            if rootA == rootB:
                return False
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return False
        
        return True

