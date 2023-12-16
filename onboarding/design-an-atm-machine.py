class ATM:
    def __init__(self):
        self.banknotes = [0] * 5
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotes_count: List[int]) -> None:
        for i in range(5):
            self.banknotes[i] += banknotes_count[i]
    def withdraw(self, amount: int) -> List[int]:
        res = [0, 0, 0, 0, 0]
        for i in range(4, -1, -1):
            res[i] = min(amount // self.values[i], self.banknotes[i])
            amount -= res[i] * self.values[i]

        if amount == 0:
            self.deposit([-x for x in res])
            return res
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)