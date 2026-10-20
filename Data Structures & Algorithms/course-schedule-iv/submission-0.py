class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = defaultdict(list)
        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]
            graph[a].append(b)
        
        answer = [False] * len(queries)

        queue = deque()
        for i in range(len(queries)):
            queue.clear()
            queue.append(queries[i][0])
            found = False

            while queue:
                if found:
                    break
                curr = queue.popleft()
                for nei in graph[curr]:
                    if nei == queries[i][1]:
                        found = True
                        answer[i] = True
                    else:
                        queue.append(nei)
            
            if not found:
                answer[i] = False
        
        return answer
            


        