class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maximum = max(maximum, area)
            if heights[left] <= heights[right]: # remember to move inwards since lower height is limiting
                left+=1
            else:
                right -=1
        
       
       
        return maximum