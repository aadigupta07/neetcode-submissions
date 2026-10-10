class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # tracking latest occurence of each letter once
        
        latest = defaultdict(int)
        for i in range(len(s)):
            latest[s[i]] = i
        
        # want to go through, and close the interval once the latest of each letter seen so far in that interval
        # might need second point to represent start
        
        result = []
        last = -1
        l = 0
        for r in range(len(s)):
            last = max(last, latest[s[r]])
            if r == last: # means you hit the last element where r is last element
                result.append(r-l+1)
                l = r+1
                last = -1
        
        return result




            