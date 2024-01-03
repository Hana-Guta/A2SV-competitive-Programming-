class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(st) - 1
        
        while left <= right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1

        return True