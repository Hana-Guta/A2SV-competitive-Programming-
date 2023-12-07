class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = current_week = daily_sum = 0
    
        for day in range(n):
            if day % 7 == 0:
                current_week += 1
                daily_sum = current_week
            else:
                daily_sum += 1
            total_money += daily_sum
        return total_money