class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]: 
        graph = defaultdict(list)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        result = [0] * len(queries)
        
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            
            if a not in graph:
                result[i] = -1.0
                continue
            if a == b:
                result[i] = 1.0
                continue
            
            visited = set(a)
            queue = deque([(a, 1.0)])
            found = False
            while queue and not found:
                curr, answer = queue.popleft()
                
                for nei, val in graph[curr]:
                    if nei in visited:
                        continue
                    if nei == b:
                        result[i] = answer * val
                        found = True
                        break
                    else:
                        queue.append((nei, answer * val))
                        visited.add(nei)
            if not found:
                result[i] = -1.0
        
        return result
                

        
                
            

            
            


        
