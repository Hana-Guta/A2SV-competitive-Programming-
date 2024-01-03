class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        count = left = right = 0 

        while left<len(g) and right<len(s):
            if g[left] <= s[right]:
                count += 1
                left += 1
                right += 1
            else:
                left += 1

        return count