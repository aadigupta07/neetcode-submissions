class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s)) # just need to remember to use sorted string as key and you are good
            sets[key].append(s)
        
        return list(sets.values()) # also returning list of values
