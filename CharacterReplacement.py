class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0 
        char_count = [0] * 26  

        left = 0
        for right in range(len(s)):
            char_count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, char_count[ord(s[right]) - ord('A')])

            replacements_needed = (right - left + 1) - max_count

            if replacements_needed > k:
                
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
