class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            n = int(s[i])
            i += 2
            result.append(s[i:i+n])
            i += n
        
        return result

        