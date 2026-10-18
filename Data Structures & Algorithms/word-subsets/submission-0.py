from collections import defaultdict, Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        count2 = defaultdict(int)
        for word in words2:
            current = defaultdict(int)
            for c in word:
                current[c] += 1
                count2[c] = max(count2[c], current[c])
        
        n = len(count2)
        
        ongoing = defaultdict(int)
        
        for word in words1:
            needed = n
            ongoing.clear()
            for c in word:
                ongoing[c] += 1
                if c in count2 and ongoing[c] == count2[c]:
                    needed-=1
                if needed == 0:
                    result.append(word)
                    break
        
        return result
                    



                
                
