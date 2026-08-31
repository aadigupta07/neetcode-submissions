class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ']' or c == ')' or c == '}':
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if c == ']' and a != '[':
                        return False
                    if c == ')' and a != '(':
                        return False
                    if c == '}' and a != '{':
                        return False
            else:
                stack.append(c)



        return not stack