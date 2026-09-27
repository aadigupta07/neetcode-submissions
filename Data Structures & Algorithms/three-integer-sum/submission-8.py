class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while r >0 and nums[r] == nums[r-1]:
                        r-=1
                    r-=1
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                elif total < 0:
                    
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                else:
                    while r >0 and nums[r] == nums[r-1]:
                        r-=1
                    r-=1
                
        return result