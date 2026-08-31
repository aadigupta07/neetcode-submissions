class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(f"{len(s)}#{s}")
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        res = []
        length = len(s)
        i = 0
        while i < length:
            j = i
            while s[j] != '#':
                j+=1
            num = int(s[i:j])
            res.append(s[j+1:j + 1 + num])
            i = num + j + 1

        return res
            
            

            
        