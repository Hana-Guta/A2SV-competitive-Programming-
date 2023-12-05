class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        stg = ""
        
        for i in range(len(s)):
            st = s[indices.index(i)]
            stg += st

        return stg
            