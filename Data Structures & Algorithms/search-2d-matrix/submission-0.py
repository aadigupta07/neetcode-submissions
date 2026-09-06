class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) -1

        while l <= r:
            mid = (l+r)//2
            first = mid // len(matrix[0])
            second = mid % len(matrix[0])
            curr = matrix[first][second]
            if curr == target:
                return True
            elif curr > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False