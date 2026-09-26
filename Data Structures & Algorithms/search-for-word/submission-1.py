class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        height = len(board)
        width = len(board[0])
        visited = set() # track coordinates seen so far
        self.found = False

        def backtrack(index, path, row, col):
            if row == height or col == width or row < 0 or col < 0:
                return
            if board[row][col] != word[index]:
                return
            if (row, col) in visited:
                return
            if index == len(word) - 1:
                self.found = True
                return
            
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            
            visited.add((row, col))
            path.append(board[row][col])
            for direction in directions:
                if self.found:
                    return
                row += direction[0]
                col += direction[1]
                index +=1
                backtrack(index, path, row, col)
                index -=1
                row -= direction[0]
                col -= direction[1]
            path.pop()
            visited.remove((row, col))
            
            

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrack(0, [], i, j)
        
        return self.found
            