class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = len(s)
        for i in range(l//2):
            
            if s[i] != s[l-1-i]:
                s[i], s[l-1-i] = s[l-1-i], s[i]
        