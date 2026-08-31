class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      greater = {}
      stack = []

      for num in nums2:
        while stack and num > stack[-1]:
            popped = stack.pop()
            greater[popped] = num
        
        stack.append(num)
    
      return [greater.get(num, -1) for num in nums1]
