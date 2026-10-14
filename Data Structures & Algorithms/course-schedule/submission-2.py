class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        

        queue = deque()
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return len(order) == numCourses

