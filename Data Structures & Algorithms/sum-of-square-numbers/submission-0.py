class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c+1):
            for j in range(i, c+1):
                if i**2 + j**2 == c:
                    return True
        
        return False
