class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        seen = {}
        Lngt = 0
        start = 0

        for i in range(n):
            if s[i] in seen:
                start = max(start, seen[s[i]] + 1)
                
            seen[s[i]] = i
            Lngt = max(Lngt, i - start + 1)

        return Lngt
        



