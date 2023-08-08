class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        start = 0
        end = 0
        
        for i in range(len(s)):
            last = s.rindex(s[i])
            
            if last > end:
                end = last
            if end == i:
                ans.append(end - start + 1)
                start = end + 1
        return ans
