class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        highest = 1
        for num in nums:
            if num-1 in check:
                continue
            else:
                count = 1
                while True:
                    if num + 1 in check:
                        count +=1
                        highest = max(highest, count)
                    else:
                        break
                    num += 1
        
        return highest
                
