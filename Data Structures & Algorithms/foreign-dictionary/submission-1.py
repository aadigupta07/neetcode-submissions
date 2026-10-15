class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        letters = set()
        for word in words:
            for c in word:
                letters.add(c)
        
        for letter in letters:
            indegree[letter] = 0

        # graph building
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j = 0
            found = False
            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]]+=1
                    found = True
                    break
                
                j+=1
            
            if not found and len(word1) > len(word2):
                return ""
        
        # populating the queue
        queue = deque()
        for key in indegree:
            if indegree[key] == 0:
                queue.append(key)
        
        # bfs and final result
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(result) != len(letters):
            return ""
        return "".join(result)
        
        
                

        


                
            
            
                