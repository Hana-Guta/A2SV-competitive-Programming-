class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = Counter(s)
        
        for key, value in count.items():
            if value > 1 :
                count[key] = 1

        return sum(count.values())

