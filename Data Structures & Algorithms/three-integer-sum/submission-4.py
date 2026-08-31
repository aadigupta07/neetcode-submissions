class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        seen = {}
        for i in range(0, len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    right -=1
                    while nums[right] == nums[right+1] and right > left:
                        right -=1
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1

                    continue
                if sum > 0:
                    right -=1
                    while nums[right] == nums[right+1] and right > left:
                        right -=1
                if sum < 0:
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        
        return result
                    

