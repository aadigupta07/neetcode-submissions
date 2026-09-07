class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')' : '(', ']' : '[', '}' : '{'}
        # useful to remember pairing, with closing first

        for c in s:
            if c in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c) # only every append openings, compare closings
        
        return not stack