class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.zeros = set(range(0, size))
        self.ones = set()
        self.total = 0
        

    def fix(self, idx: int) -> None:
        if idx not in self.ones:
            self.zeros.remove(idx)
            self.ones.add(idx)
            self.total += 1

    def unfix(self, idx: int) -> None:
        if idx not in self.zeros:
            self.ones.remove(idx)
            self.zeros.add(idx)
            self.total -= 1
        

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones
        self.total = self.size - self.total

    def all(self) -> bool:
        return self.total == self.size
        

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return self.total

    def toString(self) -> str:
        res = []

        for idx in range(self.size):
            if idx in self.zeros:
                res.append("0")

            else:
                res.append("1")

        return "".join(res)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()  change it a littele bit