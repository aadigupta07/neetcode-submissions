class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, inners):
            if len(path) - inners > inners:
                return
            if inners > n:
                return
            if len(path) == 2 * n:
                result.append("".join(path[:]))
                return
            
            
            
            path.append("(")
            backtrack(path, inners+1)
            path.pop()
            path.append(")")
            backtrack(path, inners)
            path.pop()
        
        backtrack([], 0)
        return result
            
