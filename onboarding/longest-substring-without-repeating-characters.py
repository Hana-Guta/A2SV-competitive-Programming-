class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window  = Counter()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            window += Counter(s[right])

            while len(window) != right - left + 1:
                window -= Counter(s[left])
                left += 1

            max_len = max(max_len , right - left + 1)

        return max_len


