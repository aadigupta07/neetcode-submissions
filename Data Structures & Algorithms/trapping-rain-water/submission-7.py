class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # if its too hard use before and after arrays
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total = 0
        
        while left < right:
            if left_max < right_max: # look at order for these before and understand how it makes sense to increment left and then check left_max with current height (height[left])
                left += 1
                left_max = max(left_max, height[left]) 
                total += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total += right_max - height[right]
        
        return total