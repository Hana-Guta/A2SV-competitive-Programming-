class RandomizedSet:

    def __init__(self):
        self.values = []
        self.idx_val = {}

    def insert(self, val: int) -> bool:
        
        if val in self.idx_val:
            return False 
        
        self.values.append(val)
        self.idx_val[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_val:
            return False 

        removed = self.idx_val[val]

        last = self.values[-1]

        self.values[removed] = last

        self.idx_val[last] = removed

        self.values.pop()
        del self.idx_val[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
