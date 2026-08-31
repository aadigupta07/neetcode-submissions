class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        end = len(nums)-1
        for i in range(0, end-1):
            j,k, target = i+1, end, -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -=1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1





        return result