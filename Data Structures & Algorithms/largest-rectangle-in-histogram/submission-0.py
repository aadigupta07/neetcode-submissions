class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, height in enumerate(heights):
            if not stack or height >= stack[-1][1]:
                stack.append((i, height))
            else:
                start = i
                while stack and stack[-1][1] > height:
                    index, h = stack.pop()
                    area = max(area, h * (i - index))
                    start = index

                stack.append((start, height))

        for i, h in stack:
            area = max(area, h * (len(heights) - i))
            
        return area
