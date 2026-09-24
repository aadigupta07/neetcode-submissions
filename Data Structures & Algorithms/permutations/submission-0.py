class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                backtrack(path)
                path.pop()
                visited.remove(nums[i])
        
        backtrack([])
        return result