class Solution:
    def reverse(self, x: int) -> int:
            
        MAX = 2**31 - 1
        MIN = -2**31

        if x >= 0:
            sign = 1
        else:
            sign = -1
        x = abs(x)

        reversed_num = 0
        while x != 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        reversed_num *= sign

        if reversed_num > MAX or reversed_num < MIN:
            return 0

        return reversed_num

