class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        combined.sort()
        
        stack = []
        for i in range(len(position)):
            time = (target-combined[i][0])/combined[i][1]
            
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)
            
                
            

                
            