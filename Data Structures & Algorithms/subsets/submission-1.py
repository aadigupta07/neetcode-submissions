class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        def backtrack(start, path):
            result.append(path[:])

            if len(path) == len(nums):
                return
            
            for i in range(start, len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
                visited.remove(nums[i])
            
                    
        backtrack(0, [])
        return result
        

