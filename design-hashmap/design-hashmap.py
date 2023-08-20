class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash_function(key)
        if self.map[index] is None:
            self.map[index] = []
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash_function(key)
        if self.map[index] is None:
            return -1
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash_function(key)
        if self.map[index] is None:
            return
        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                del self.map[index][i]
                return
