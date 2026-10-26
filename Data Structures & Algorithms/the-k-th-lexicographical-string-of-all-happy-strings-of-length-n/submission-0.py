class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(path):
            if len(result) == k:
                return
            if len(path) == n:
                result.append("".join(path))
                return
            
            for char in ('a', 'b', 'c'):
                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()

        backtrack([])
        if len(result) < k:
            return ""
        return result[-1]
