class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        before = [0] * n
        after = [0] * n
        before[0] = height[0]
        after[n-1] = height[n-1]
        total = 0

        for i in range (1, n):
            before[i] = max(before[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            after[i] = max(after[i+1], height[i])
        
        for i in range(1,n-1):
            curr = min(before[i], after[i]) - height[i]
            total += curr if curr > 0 else 0
        
        return total