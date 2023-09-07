class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = deque()
        self.value_count = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        self.value_count[num] += 1

        if len(self.stream) > self.k:
            removed_num = self.stream.popleft()
            self.value_count[removed_num] -= 1
            if self.value_count[removed_num] == 0:
                del self.value_count[removed_num]

        return self.value_count.get(self.value, 0) == self.k

