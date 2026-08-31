class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        before = [0] * length
        after = [0] * length
        before[0] = height[0]
        after[length-1] = height[length-1]
        total = 0
        
        for i in range(1, length):
            before[i] = before[i-1]
            if height[i] > before[i-1]:
                before[i] = height[i]
        
        for i in range (length-2, -1, -1):
            after[i] = after[i+1]
            if height[i] > after[i+1]:
                after[i] = height[i]
            

        for i in range(1, length-1):
            total += min(before[i], after[i]) - height[i]
        

        return total