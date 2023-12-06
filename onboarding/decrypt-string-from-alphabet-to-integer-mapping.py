class Solution:
    def freqAlphabets(self, s: str) -> str:
        stg = ""
        right = len(s)-1
        while right >= 0:
            if s[right]=="#":
                stg += chr(int(s[right-2:right])+96)
                right -= 2
            else:
                stg += chr(int(s[right] )+96)
            right -= 1
        return stg[::-1]
        