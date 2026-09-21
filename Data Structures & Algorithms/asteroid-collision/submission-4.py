class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for curr in asteroids:
            alive = True
            while alive and stack and curr < 0 and stack[-1] > 0:
                if abs(curr) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(curr) == abs(stack[-1]):
                    stack.pop()
                alive = False

            if alive:
                stack.append(curr)

        return stack