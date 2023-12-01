class Solution:
    def romanToInt(self, s: str) -> int:
        N = len(s)
        Dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,"M":1000}

        total = 0
        
        for i in range(N):
            if i < N - 1 and Dict[s[i]] < Dict[s[i+1]]:
                total -= Dict[s[i]]
            else:
                total += Dict[s[i]]
        
        return total