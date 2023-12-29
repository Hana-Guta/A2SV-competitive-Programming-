class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = int(copysign(1, num))
        num = abs(num)

        if num == 0:
            return 0

        if sign == -1:
            digits = sorted(str(num), reverse=True)
            return sign * int("".join(digits))
        else:
            digits = sorted(str(num))
            zeros = digits.count('0')

            if zeros != 0:
                digits[0], digits[zeros] = digits[zeros], digits[0]

            return sign * int("".join(digits))
