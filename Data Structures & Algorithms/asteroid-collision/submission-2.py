class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr in asteroids:
            equal = False
            if not stack or curr * stack[-1] > 0:
                stack.append(curr)
                continue
            else:
                while stack and curr < 0 and stack[-1] > 0 and abs(curr) >= abs(stack[-1]):
                    

                    
                    if stack and abs(curr) == abs(stack[-1]):
                        stack.pop()
                        equal = True
                        break
                    stack.pop()
                
            if not equal and (not stack or curr * stack[-1] > 0):
                    stack.append(curr)
                
        return stack
