class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(set)
        
        indegree = [0] * numCourses
        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]
            graph[a].add(b)
            indegree[b] += 1
        
        

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0: # i is root, everything in bfs of i, i should point to
                queue.append(i)
                while queue:
                    curr = queue.popleft()
                    for nei in graph[curr]:
                        graph[i].add(nei)
                        queue.append(nei)


        answer = [False] * len(queries)

        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if b in graph[a]:
                answer[i] = True
        
        return answer

        
        
        
                
        
            


        