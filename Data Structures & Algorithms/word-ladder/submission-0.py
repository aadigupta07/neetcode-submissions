class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # need to represent graph, undirected, where a one letter difference means there is an edge
        # just do bfs after creating this graph
        # mapping[*lock] = [clock, block, flock]
        mapping = defaultdict(list)

        # making the keys
        for word in wordList:
            for i in range(len(word)):
                string = "".join([word[0:i],"*",word[i+1:]])
                mapping[string].append(word)

        queue = deque()
        queue.append(beginWord)
        visited = set()
        dist = 1

        while queue:
            print(queue)
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return dist

                for i in range(len(word)):
                    string = "".join([word[0:i],"*",word[i+1:]])
                    neighbors = mapping[string]

                    for nei in neighbors:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            
            dist+=1
        
        return 0








        


        

        
        
            
                
                




