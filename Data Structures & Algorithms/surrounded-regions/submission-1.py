class Solution:
    def solve(self, board: List[List[str]]) -> None:

        queue = deque()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1 or j == 0 or j == len(board[0])-1) and board[i][j] == "O":
                    
                    queue.append((i, j))
                    board[i][j] = "T"
        
        while queue:
            r, c = queue.popleft()

            for a, b in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nr, nc = r + a, c + b
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue
                elif board[nr][nc] == "X" or board[nr][nc] == "T":
                    continue
                else:
                    board[nr][nc] = "T"
                    queue.append((nr, nc))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
                
        

