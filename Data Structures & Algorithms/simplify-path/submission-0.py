class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split_path = path.split('/')

        for c in split_path:
            if c == '' or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return '/' + '/'.join(stack)