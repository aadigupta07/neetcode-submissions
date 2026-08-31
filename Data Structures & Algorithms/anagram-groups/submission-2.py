class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            sets[key].append(s)
        
        return list(sets.values())
