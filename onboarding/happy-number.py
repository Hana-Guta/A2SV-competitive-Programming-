class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_number(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit ** 2
                num //= 10
            return total_sum
    
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next_number(n)
    
        return n == 1