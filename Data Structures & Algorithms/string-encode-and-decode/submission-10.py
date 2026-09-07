class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}") # tracking len and unique character
        
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#": # making sure you account for double digit lengths
                j += 1
            n = int(s[i:j])
            i = j + 1
            result.append(s[i:i+n])
            i += n
        
        return result

        