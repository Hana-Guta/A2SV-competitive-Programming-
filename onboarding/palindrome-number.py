class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        int_x = x

        if x < 0 :
            return False
        while x != 0:
            y = (y*10) + x % 10
            x = x // 10

        if y == int_x :
            return True
        return False
        

        