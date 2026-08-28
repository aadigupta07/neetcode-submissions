class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        count = 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                cookie += 1
                child += 1
                count += 1
            
            else:
                cookie += 1
        return count