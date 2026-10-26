class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        best = 0
        for i in range(len(matrix)):
            row = sorted(matrix[i], key=lambda x: -x)
            width = 1
            for j in range(len(matrix[0])):
                best = max(best, row[j] * width)
                width+=1
        
        return best
                
                



        
                
        