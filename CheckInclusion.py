class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        if len(s1) > len(s2):
            return False
        
        window_count = Counter(s2[:len(s1)])
        target_count = Counter(s1) 
        if window_count == target_count:
            return True
        
        for i in range(1, len(s2) - len(s1) + 1):
            if window_count[s2[i - 1]] == 1:
                del window_count[s2[i - 1]]
            else:
                window_count[s2[i - 1]] -= 1
            window_count[s2[i + len(s1) - 1]] += 1
            
            if window_count == target_count:
                return True
        
        return False


