class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        path = []
        def backtrack(path, index):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            

            for j in range(len(mapping[digits[index]])):
                path.append(mapping[digits[index]][j])
                backtrack(path, index+1)
                path.pop()
        
        backtrack([], 0)
        return result

            
