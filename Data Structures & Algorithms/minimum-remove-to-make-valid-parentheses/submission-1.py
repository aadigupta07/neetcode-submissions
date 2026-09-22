class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = {}
        result = [''] * len(s)

        # get valid parentheses with indices
        for i, c in enumerate(s):
            if c != ')' and c != '(':
                continue
            if c == ')':
                if not stack:
                    continue
                else:
                    first = stack.pop()
                    valid[first[0]] = first[1]
                    valid[i] = c
            else:
                stack.append((i,c))
        
        for i, c in enumerate(s):
            if c != '(' and c != ')':
                result[i] = c
                continue
            if i in valid:
                result[i] = valid[i]
            else:
                continue
            
            


            
        result = [c for c in result if c != '']
        return "".join(result)


