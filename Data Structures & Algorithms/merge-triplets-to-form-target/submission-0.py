class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check1 = False
        check2 = False
        check3 = False
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                check1 = True
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                check2 = True
            if triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                check3 = True
        
        return check1 and check2 and check3
        
            