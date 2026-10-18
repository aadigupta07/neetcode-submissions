class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute force is bfs spawning from each tracking longest increasing path
        # dp improvement could track path length from each square
        # 

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
            
        
        def dfs(r, c, val):
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0 
            if matrix[r][c] <= val:
                return 0 
            if dp[r][c] > 0:
                return dp[r][c]
            
            result = 1
            result = max(result, 1 + dfs(r - 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r + 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c - 1, matrix[r][c]))
            result = max(result, 1 + dfs(r, c + 1, matrix[r][c]))
            dp[r][c] = result
            return result
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, float('-inf'))
        
        return max([max(row) for row in dp])
            



                    