class FrequencyTracker:

    def __init__(self):
        self.freq1 = defaultdict(int)
        self.freq2 = defaultdict(int)
        
    def add(self, number: int) -> None:
        if self.freq1[number] in self.freq2 and number in self.freq1:
            self.freq2[self.freq1[number]] -= 1
        self.freq1[number] += 1
        self.freq2[self.freq1[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq1[number] > 0:
            self.freq2[self.freq1[number]] -= 1
            self.freq1[number] -= 1
            self.freq2[self.freq1[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq2[frequency] != 0
