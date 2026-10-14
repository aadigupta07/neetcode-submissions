class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(order) == numCourses:
            return order
        else:
            return []

