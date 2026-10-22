class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)), -1, -1):
            first = a**2
            second = c - first
            if math.sqrt(second).is_integer():
                return True
        
        return False


